import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.hostedcheckout.create_hosted_checkout_request import CreateHostedCheckoutRequest
from ingenico.connect.sdk.domain.hostedcheckout.definitions.hosted_checkout_specific_input import HostedCheckoutSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.customer import Customer
from ingenico.connect.sdk.domain.payment.definitions.order import Order
from ingenico.connect.sdk.domain.payment.definitions.customer_base import CustomerBase

configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),'./configuracion.ini'))
api_key_id = os.getenv("connect.api.apiKeyId", "2028d86b7bc19213")
secret_api_key = os.getenv("connect.api.secretApiKey", "bqz9C3UtR7MMO3zXL/v9uAwXSlnoUAXbn2wGbXeRo0w=")
client = Factory.create_client_from_file(configuration_file_name=configuration_file_name,api_key_id=api_key_id, secret_api_key=secret_api_key)


hosted_checkout_specific_input = HostedCheckoutSpecificInput()
hosted_checkout_specific_input.locale = "en_GB"
hosted_checkout_specific_input.variant = "testVariant"
hosted_checkout_specific_input.merchantCustomerId = "3738"

amount_of_money = AmountOfMoney()
amount_of_money.amount = 2345
amount_of_money.currency_code = "USD"

billing_address = Address()
billing_address.country_code = "US"

customer = Customer()
customer.billing_address = billing_address


data = CustomerBase()
data.merchantCustomerId = "3738"



order = Order()
order.amount_of_money = amount_of_money
order.customer = customer


body = CreateHostedCheckoutRequest()
body.hosted_checkout_specific_input = hosted_checkout_specific_input

body.order = order

print(client.merchant("3738").hostedcheckouts().create(body))

response = client.merchant("3738").hostedcheckouts().create(body)


