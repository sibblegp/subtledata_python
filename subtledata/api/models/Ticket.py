#!/usr/bin/env python
"""
Copyright 2012 Wordnik, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class Ticket:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'date_closed': 'str',
            'tax': 'float',
            'date_opened': 'str',
            'total': 'float',
            'location_id': 'int',
            'employee_id': 'int',
            'ticket_open': 'bool',
            'pre_auth_payments': 'list[PreAuthPayment]',
            'remaining_balance': 'float',
            'ticket_id': 'int',
            'table_name': 'str',
            'revenue_center_id': 'int',
            'user_id': 'int',
            'pre_auth_cards': 'list[PreAuthCard]',
            'discount': 'float',
            'external_payments': 'list[ExternalPayment]',
            'cover_count': 'int',
            'subtotal': 'float',
            'service_charge': 'float',
            'date_modified': 'str',
            'items': 'list[Item]',
            'pos_ticket_id': 'int',
            'table_id': 'int',
            'payments': 'list[Payment]',
            'connected_users': 'list[ConnectedUser]'

        }


        #Date Closed (UTC)
        self.date_closed = None # str
        #Tax amount
        self.tax = None # float
        #Date Opened (UTC)
        self.date_opened = None # str
        #Total amount
        self.total = None # float
        #Location ID
        self.location_id = None # int
        #Employee ID
        self.employee_id = None # int
        #Ticket open/closed status
        self.ticket_open = None # bool
        self.pre_auth_payments = None # list[PreAuthPayment]
        #Ticket remaining balance
        self.remaining_balance = None # float
        #Ticket ID
        self.ticket_id = None # int
        #Table Name
        self.table_name = None # str
        #Revenue Center ID
        self.revenue_center_id = None # int
        #User ID
        self.user_id = None # int
        self.pre_auth_cards = None # list[PreAuthCard]
        #Discount amount
        self.discount = None # float
        self.external_payments = None # list[ExternalPayment]
        #Cover Count
        self.cover_count = None # int
        #Subtotal amount
        self.subtotal = None # float
        #Service charge
        self.service_charge = None # float
        #Date Modified (UTC)
        self.date_modified = None # str
        self.items = None # list[Item]
        #POS System Ticket Identifier
        self.pos_ticket_id = None # int
        #Table ID
        self.table_id = None # int
        self.payments = None # list[Payment]
        self.connected_users = None # list[ConnectedUser]
        
