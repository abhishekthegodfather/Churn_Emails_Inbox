class churn_mail:
    def __init__(self, file_name):
        self.file_name = file_name
        
    def number_of_lines(self):
        with open(self.file_name) as file:
            data = file.read()
        count_num_lines = 0
        for i in data:
            if i == '\n':
                count_num_lines += 1
        return count_num_lines
    
    def count_number_of_line(self):
        count_num_subjects = 0
        file_read = open(self.file_name)
        for i in file_read:
            line = i.rstrip()
            if line.startswith('Subject:'):
                count_num_subjects += 1
        return count_num_subjects
    
    def avarage_spam_confidence(self):
        file_read = open(self.file_name)
        count_total = 0
        spam_confidence = 0
        for i in file_read:
            line = i.rstrip()
            if line.startswith('X-DSPAM-Confidence:'):
                value = line.split(':')
                spam_confidence += float(value[1])
                count_total += 1
        return spam_confidence/count_total
    
    def find_email_send_days(self):
        file_read = open(self.file_name)
        day_dict = {}
        for line in file_read:
            line = line.rstrip()
            if line.startswith('From '):
                day = line.split(" ")[2].strip()
                day_dict[day] = day_dict.get(day, 0)+1
        return day_dict 
    
    def count_message_from_email(self):
        file_read = open(self.file_name)
        count = 0
        email_dict = {}
        for line in file_read:
            line = line.rstrip()
            if line.startswith('From:') and '@' in line:
                email = line.split(" ")[1].strip()
                count += 1
                email_dict[email] = email_dict.get(email, 0)+1
        return email_dict
    
    def count_message_from_domain(self):
        file_read = open(self.file_name)
        count = 0
        domain_dict = {}
        for line in file_read:
            line = line.rstrip()
            if line.startswith('From:') and '@' in line:
                email = line.split(" ")[1].strip()
                domain = email.split('@')[1]
                if domain not in domain_dict:
                    domain_dict[domain] = 1
                else:
                    domain_dict[domain] += 1
        return domain_dict



mail = churn_mail("mbox-short.txt")
print("The number of lines in the churn_mail dataset",mail.number_of_lines())

print("The number of subject lines in the churn_mail dataset",mail.count_number_of_line())


print("The Average Spam Confidence in the churn_mail dataset",mail.avarage_spam_confidence())


print()
print("The Day of the Week the Email was sent in the churn_mail dataset")
print(mail.find_email_send_days())


print()
print("Counting the Number of Messages From Each Email Address in the churn_mail dataset")
print(mail.count_message_from_email())


print()
print("Counting the Number of Messages From Each Domain in the churn_mail dataset")
print(mail.count_message_from_domain())