from fastapi import APIRouter
import pandas as pd
from app.config import db, commit_rollback

from app.models import Users
from app.models.compound import Compound
from app.models.experiment import Experiment
from app.models.experiment_compound import ExperimentCompound
from app.repository.CompoundRepository import CompoundRepository
from app.repository.ExperimentCompoundRepository import ExperimentCompoundRepository
from app.repository.ExperimentRepository import ExperimentRepository
from app.repository.UsersRepository import UsersRepository

router = APIRouter(
    prefix="/etl",
    tags=['etl']
)

def chunker(size, seq):
    for i in range(0, len(seq), size):
        yield seq[i:i+size]

def clean_columns(columns):
    return [col.strip() for col in columns]

def clean_rows(df):
    return df.map(lambda x: x.strip() if isinstance(x, str) else x)


@router.post("/")
async def run_etl():
    # Load CSV files
    users_df = pd.read_csv('app/data/users.csv')
    user_experiments_df = pd.read_csv('app/data/user_experiments.csv')
    compounds_df = pd.read_csv('app/data/compounds.csv')

    # clean data
    # clean column names
    compounds_df.columns = clean_columns(compounds_df.columns)
    users_df.columns = clean_columns(users_df.columns)
    user_experiments_df.columns = clean_columns(user_experiments_df.columns)

    # clean rows
    users_df = clean_rows(users_df)
    user_experiments_df = clean_rows(user_experiments_df)
    compounds_df = clean_rows(compounds_df)

    # 1. Total experiments a user ran
    total_experiments_per_user = user_experiments_df.groupby('user_id')['experiment_id'].count()

    # 2. Average experiments amount per user
    average_experiments_per_user = total_experiments_per_user.mean()

    # 3. User's most commonly experimented compound
    split_df = user_experiments_df['experiment_compound_ids'].str.split(';', expand=True)
    split_df = split_df.stack().reset_index(level=1, drop=True).reset_index(name='compound')
    split_df['compound'] = split_df['compound'].str.strip()

    merged_df = user_experiments_df.merge(split_df, left_index=True, right_on='index')

    grouped = merged_df.groupby(['user_id', 'compound']).size()
    most_common_compound_per_user = grouped.groupby('user_id').idxmax().apply(lambda x: x[1])

    users = []
    for idx, read_user in users_df.iterrows():
        id = read_user['user_id']
        users.append(Users(
            user_id=id,
            name=read_user['name'],
            email=read_user['email'],
            signup_date=read_user['signup_date'],
            total_experiments=total_experiments_per_user[id],
            avg_experiments=average_experiments_per_user,
            common_compound=most_common_compound_per_user[id]))
        
    await UsersRepository.create_all(users)
        
    compounds = []
    for idx, compound in compounds_df.iterrows():
        compounds.append(Compound(
            compound_id=compound['compound_id'],
            compound_name=compound['compound_name'],
            compound_structure=compound['compound_structure'],
        ))


    await CompoundRepository.create_all(compounds)

    experiments = []
    for idx, read_user_experiment in user_experiments_df.iterrows():
        experiments.append(Experiment(
            experiment_id=read_user_experiment['experiment_id'],
            experiment_run_time=read_user_experiment['experiment_run_time'],
            user_id=read_user_experiment['user_id']))      
        
    await ExperimentRepository.create_all(experiments)

    experiment_compounds = []
    for idx, experiment_compound in split_df.iterrows():
        experiment_compounds.append(ExperimentCompound(
            experiment_id=experiment_compound['index']+1,
            compound_id=experiment_compound['compound']))
        
    await ExperimentCompoundRepository.create_all(experiment_compounds)
    
    return {"status": "success"}
