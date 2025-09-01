# RL Agent Training Script
from stable_baselines3 import DQN
from env import MicroserviceDeploymentEnv

env = MicroserviceDeploymentEnv()
model = DQN('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=10000)
model.save('dqn_microservice')
