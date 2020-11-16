import gym
from stable_baselines import PPO2
from stable_baselines.common.policies import MlpPolicy


def main():
    env = gym.make('CartPole-v1')
    # Optional: PPO2 requires a vectorized environment to run
    # the env is now wrapped automatically when passing it to the constructor
    # env = DummyVecEnv([lambda: env])

    model = PPO2(MlpPolicy, env, verbose=1)
    model.learn(total_timesteps=10000)

    obs = env.reset()
    for i in range(1000):
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        env.render()

    env.close()


if __name__ == '__main__':
    main()
