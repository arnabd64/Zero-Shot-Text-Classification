FROM python:3.11-slim-bookworm

RUN useradd -m user
ENV USER=user
ENV HOME=/home/${USER}
ENV PATH=${HOME}/.local/bin:$PATH
USER ${USER}
WORKDIR ${HOME}/app

COPY --chown=${USER}:${USER} pyproject.toml .
RUN pip install --user poetry  && \
    poetry install

COPY --chown=${USER}:${USER} . .

CMD ["poetry", "run", "python", "main.py"]