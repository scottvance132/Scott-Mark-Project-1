import pytest

import dao.reimbursement_dao
from model.reimbursement import Reimbursement
from service.reimbursement_service import ReimbursementService
from dao.reimbursement_dao import ReimbursementDao
from exceptions.invalid_parameter_error import InvalidParameterError


def test_get_all_reimb_by_user_id(mocker):
    def mock_get_all_reimb_by_user_id(self, reimb_author):
        return[Reimbursement(1, 200, '2022-07-26 13:49:50.507', None, 'pending', 'Food', 'Lunch', 'receipt.jpeg', 'joey21', None),
               Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg', 'joey21', None)]

    mocker.patch('dao.reimbursement_dao.ReimbursementDao.get_all_reimb_by_user_id', mock_get_all_reimb_by_user_id)

    reimb_service = ReimbursementService()

    actual = reimb_service.get_all_reimb_by_user_id('joey21', None)

    assert actual == [
        {
            'reimb_id': 1,
            'amount': 200,
            'submitted': '2022-07-26 13:49:50.507',
            'resolved': None,
            'status': 'pending',
            'type': 'Food',
            'description': 'Lunch',
            'receipt': 'receipt.jpeg',
            'author': 'joey21',
            'resolver': None
        },
        {
            'reimb_id': 2,
            'amount': 1200,
            'submitted': '2022-07-26 13:49:50.507',
            'resolved': None,
            'status': 'approved',
            'type': 'Lodging',
            'description': 'Hotel',
            'receipt': 'receipt.jpeg',
            'author': 'joey21',
            'resolver': None
        }
    ]


def test_get_all_reimb_by_user_id_status(mocker):
    def mock_get_all_reimb_by_user_id_status(self, reimb_author, query):
        return[Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg', 'joey21', None)]

    mocker.patch('dao.reimbursement_dao.ReimbursementDao.get_all_reimb_by_user_id_status', mock_get_all_reimb_by_user_id_status)

    reimb_service = ReimbursementService()

    actual = reimb_service.get_all_reimb_by_user_id('joey21', 'pending')

    assert actual == [
        {
            'reimb_id': 2,
            'amount': 1200,
            'submitted': '2022-07-26 13:49:50.507',
            'resolved': None,
            'status': 'approved',
            'type': 'Lodging',
            'description': 'Hotel',
            'receipt': 'receipt.jpeg',
            'author': 'joey21',
            'resolver': None
        }
    ]


def test_get_all_reimb(mocker):
    def mock_get_all_reimb(self):
        return[Reimbursement(1, 200, '2022-07-26 13:49:50.507', None, 'pending', 'Food', 'Lunch', 'receipt.jpeg', 'joey21', None),
               Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg', 'joey221', None)]

    mocker.patch('dao.reimbursement_dao.ReimbursementDao.get_all_reimb', mock_get_all_reimb)

    reimb_service = ReimbursementService()

    actual = reimb_service.get_all_reimb(None)

    assert actual == [
        {
            'reimb_id': 1,
            'amount': 200,
            'submitted': '2022-07-26 13:49:50.507',
            'resolved': None,
            'status': 'pending',
            'type': 'Food',
            'description': 'Lunch',
            'receipt': 'receipt.jpeg',
            'author': 'joey21',
            'resolver': None
        },
        {
            'reimb_id': 2,
            'amount': 1200,
            'submitted': '2022-07-26 13:49:50.507',
            'resolved': None,
            'status': 'approved',
            'type': 'Lodging',
            'description': 'Hotel',
            'receipt': 'receipt.jpeg',
            'author': 'joey221',
            'resolver': None
        }
    ]


def test_get_all_reimb_status(mocker):
    def mock_get_all_reimb_status(self, query):
        return[Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg', 'joey21', None)]

    mocker.patch('dao.reimbursement_dao.ReimbursementDao.get_all_reimb_status', mock_get_all_reimb_status)

    reimb_service = ReimbursementService()

    actual = reimb_service.get_all_reimb('approved')

    assert actual == [
        {
            'reimb_id': 2,
            'amount': 1200,
            'submitted': '2022-07-26 13:49:50.507',
            'resolved': None,
            'status': 'approved',
            'type': 'Lodging',
            'description': 'Hotel',
            'receipt': 'receipt.jpeg',
            'author': 'joey21',
            'resolver': None
        }
    ]


def test_add_reimbursement_by_user_id_positive(mocker):

    reimb_obj_to_add = Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg', 'joey21', None)

    def mock_add_reimbursement_by_user_id(self, reimb_obj, receipt):
        if reimb_obj == reimb_obj_to_add:
            return Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg', 'joey21', None)
        else:
            return None

    mocker.patch('dao.reimbursement_dao.ReimbursementDao.add_reimbursement_by_user_id', mock_add_reimbursement_by_user_id)

    reimb_service = ReimbursementService()

    actual = reimb_service.add_reimbursement_by_user_id(reimb_obj_to_add, 'receipt.jpeg')

    assert actual == {
            'reimb_id': 2,
            'amount': 1200,
            'submitted': '2022-07-26 13:49:50.507',
            'resolved': None,
            'status': 'approved',
            'type': 'Lodging',
            'description': 'Hotel',
            'receipt': 'receipt.jpeg',
            'author': 'joey21',
            'resolver': None
        }


def test_add_reimbursement_by_user_id_negative_amount_none(mocker):

    reimb_obj_to_add = Reimbursement(2, None, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg', 'joey21', None)

    def mock_add_reimbursement_by_user_id(self, reimb_obj, receipt):
        if reimb_obj == reimb_obj_to_add:
            return Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg', 'joey21', None)
        else:
            return None

    mocker.patch('dao.reimbursement_dao.ReimbursementDao.add_reimbursement_by_user_id', mock_add_reimbursement_by_user_id)

    reimb_service = ReimbursementService()

    with pytest.raises(InvalidParameterError) as excinfo:
        actual = reimb_service.add_reimbursement_by_user_id(reimb_obj_to_add, 'receipt.jpeg')

    assert str(excinfo.value) == 'The reimbursement amount must not be blank!'


def test_add_reimbursement_by_user_id_negative_amount_not_numeric(mocker):

    reimb_obj_to_add = Reimbursement(2, 'abc', '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg', 'joey21', None)

    def mock_add_reimbursement_by_user_id(self, reimb_obj, receipt):
        if reimb_obj == reimb_obj_to_add:
            return Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg', 'joey21', None)
        else:
            return None

    mocker.patch('dao.reimbursement_dao.ReimbursementDao.add_reimbursement_by_user_id', mock_add_reimbursement_by_user_id)

    reimb_service = ReimbursementService()

    with pytest.raises(InvalidParameterError) as excinfo:
        actual = reimb_service.add_reimbursement_by_user_id(reimb_obj_to_add, 'receipt.jpeg')

    assert str(excinfo.value) == 'The reimbursement amount must be an integer!'


def test_add_reimbursement_by_user_id_negative_desc_none(mocker):

    reimb_obj_to_add = Reimbursement(2, 12, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', None, 'receipt.jpeg', 'joey21', None)

    def mock_add_reimbursement_by_user_id(self, reimb_obj, receipt):
        if reimb_obj == reimb_obj_to_add:
            return Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg', 'joey21', None)
        else:
            return None

    mocker.patch('dao.reimbursement_dao.ReimbursementDao.add_reimbursement_by_user_id', mock_add_reimbursement_by_user_id)

    reimb_service = ReimbursementService()

    with pytest.raises(InvalidParameterError) as excinfo:
        actual = reimb_service.add_reimbursement_by_user_id(reimb_obj_to_add, 'receipt.jpeg')

    assert str(excinfo.value) == 'The reimbursement description must not be blank!'


def test_add_reimbursement_by_user_id_negative_receipt_none(mocker):

    reimb_obj_to_add = Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', None, 'joey21', None)

    def mock_add_reimbursement_by_user_id(self, reimb_obj, receipt):
        if reimb_obj == reimb_obj_to_add:
            return Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg', 'joey21', None)
        else:
            return None

    mocker.patch('dao.reimbursement_dao.ReimbursementDao.add_reimbursement_by_user_id', mock_add_reimbursement_by_user_id)

    reimb_service = ReimbursementService()

    with pytest.raises(InvalidParameterError) as excinfo:
        actual = reimb_service.add_reimbursement_by_user_id(reimb_obj_to_add, 'receipt.jpeg')

    assert str(excinfo.value) == 'The reimbursement receipt must not be blank!'


def test_add_reimbursement_by_user_id_negative_type_none(mocker):

    reimb_obj_to_add = Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', None, 'Hotel', 'receipt.jpeg', 'joey21', None)

    def mock_add_reimbursement_by_user_id(self, reimb_obj, receipt):
        if reimb_obj == reimb_obj_to_add:
            return Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg', 'joey21', None)
        else:
            return None

    mocker.patch('dao.reimbursement_dao.ReimbursementDao.add_reimbursement_by_user_id', mock_add_reimbursement_by_user_id)

    reimb_service = ReimbursementService()

    with pytest.raises(InvalidParameterError) as excinfo:
        actual = reimb_service.add_reimbursement_by_user_id(reimb_obj_to_add, 'receipt.jpeg')

    assert str(excinfo.value) == 'The reimbursement type must not be blank!'


def test_update_reimbursement(mocker):
    def mock_update_reimbursement(self, reimb_obj):
        return Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg',
                             'joey21', None)

    mocker.patch('dao.reimbursement_dao.ReimbursementDao.update_reimb', mock_update_reimbursement)

    reimb_service = ReimbursementService()

    actual = reimb_service.update_reimbursement(Reimbursement(2, 1200, '2022-07-26 13:49:50.507', None, 'approved', 'Lodging', 'Hotel', 'receipt.jpeg',
                             'joey21', None))

    assert actual == {
            'reimb_id': 2,
            'amount': 1200,
            'submitted': '2022-07-26 13:49:50.507',
            'resolved': None,
            'status': 'approved',
            'type': 'Lodging',
            'description': 'Hotel',
            'receipt': 'receipt.jpeg',
            'author': 'joey21',
            'resolver': None
        }

