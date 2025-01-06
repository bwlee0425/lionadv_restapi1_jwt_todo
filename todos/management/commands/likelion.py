# todos/management/commands/likelion.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = '테스트 데이터를 생성합니다.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--total',
            default=10,
            type=int,
            help='생성할 데이터 수'
        )

    def handle(self, *args, **options):
        total = options.get('total')
        self.stdout.write(self.style.SUCCESS(f'{total}개의 데이터를 생성합니다.'))
