import os
from huggingface_hub import HfApi, Repository

if __name__ == '__main__':

    # Create an instance of HfApi
    api = HfApi()

    model_repo = r'XpucT/Deliberate'

    # filenames = api.list_repo_files(repo_id=model_repo, repo_type='model')
    # print(filenames)
        
    api.hf_hub_download(repo_id=model_repo, repo_type='model', filename='Deliberate_v6.safetensors', revision='main', local_dir = r'/home/faceswap/stable-diffusion-webui/models/Stable-diffusion')

    print('Download completed!')