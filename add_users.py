from django.contrib.auth.models import User

def create_users():
    user1 = User.objects.create_user('u1', password='p1')
    user2 = User.objects.create_user('u2', password='p2')

    print(f"Created users: {user1.username}, {user2.username}")

if __name__ == '__main__':
    create_users()
