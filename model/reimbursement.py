class Reimbursement:
    def __init__(self, reimb_id, amount, submit, resolve, status, r_type, desc, receipt, author, resolver):
        self.reimb_id = reimb_id
        self.amount = amount
        self.submit = submit
        self.resolve = resolve
        self.status = status
        self.type = r_type
        self.desc = desc
        self.receipt = receipt
        self.author = author
        self.resolver = resolver

    def to_dict(self):
        return {
            'reimb_id': self.reimb_id,
            'amount': self.amount,
            'submitted': self.submit,
            'resolved': self.resolve,
            'status': self.status,
            'type': self.type,
            'description': self.desc,
            'receipt': self.receipt,
            'author': self.author,
            'resolver': self.resolver
        }


r1 = Reimbursement(1, 100, '', '', 'pending', 'Food', 'Lobster dinner', '', '1', '')
print(r1.to_dict())
