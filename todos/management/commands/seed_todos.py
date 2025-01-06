# todos/management/commands/seed_todos.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
import random
from todos.models import Todo

User = get_user_model()

class Command(BaseCommand):
    help = 'Todo 테스트 데이터를 생성합니다.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            default=10,
            type=int,
            help='생성할 사용자 수'
        )
        parser.add_argument(
            '--todos',
            default=100,
            type=int,
            help='생성할 Todo 수'
        )

    def handle(self, *args, **options):
        user_count = options.get("users")
        todo_count = options.get("todos")

        faker = Faker("ko_KR")

        # 사용자 생성
        users = []
        for i in range(user_count):
            username = faker.user_name()
            while User.objects.filter(username=username).exists():
                username = faker.user_name()                
            user = User.objects.create_user(
                username=username,
                email=faker.email(),
                password="testpass123"
            )
            users.append(user)
            self.stdout.write("사용자 생성 : {}".format(username))
        # Todo 생성
        for i in range(todo_count):
            user = random.choice(users)
            todo = Todo.objects.create(
                user=user,
                title=faker.sentence(),
                content = faker.text(),
                is_completed=random.choice([True, False])
            )
            self.stdout.write("Todo 생성 : {}".format(todo.title))
        self.stdout.write("가상 데이터 생성 완료\n유저 총 {}명, Todo 총 {}건".format(user_count, todo_count))

            
            