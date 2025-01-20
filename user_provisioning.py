import csv
import argparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_users_from_csv(filename):
    users = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append(row)
    except FileNotFoundError:
        logging.error(f"File not found {filename}")
    return users

def provision_users(users, output_file="users.txt"):
    with open(output_file, mode="a", encoding="utf-8") as file:
        for user in users:
            file.write(f"{user['username']}:{user['email']}:{user['role']}\n")
            logging.info(f"User {user['username']} provisioned to {output_file}")

def deprovision_users(users,output_file="users.txt"):
    try:
        with open(output_file, mode="r", encoding="utf-8") as file:
            existing_users = file.readlines()
    except FileNotFoundError:
        logging.error(f"File not found {output_file}")
        return
    
    updated_users = []
    for line in existing_users:
        user_data = line.strip().split(":")
        username= user_data[0]
        user_found = False
        for user_to_delete in users:
            if username == user_to_delete['username']:
                logging.info(f"User {username} deprovisioned from {output_file}")
                user_found = True
                break
        if not user_found:
            updated_users.append(line)

    with open(output_file, mode="w", encoding="utf-8") as file:
        file.writelines(updated_users)


def main():
    parser = argparse.ArgumentParser(description="Automated User Provisioning Tool")
    parser.add_argument("action", choices=["provision", "deprovision"], help="Action to perform")
    parser.add_argument("--user-file", required=True, help="CSV file containing user data")
    parser.add_argument("--output-file",  default="users.txt", help="Output file to simulate the system")

    args = parser.parse_args()

    users = load_users_from_csv(args.user_file)

    if users:
        if args.action == "provision":
            provision_users(users, args.output_file)
        elif args.action == "deprovision":
            deprovision_users(users, args.output_file)

    else:
        logging.error("No users found")

if __name__ == "__main__":
    main()
