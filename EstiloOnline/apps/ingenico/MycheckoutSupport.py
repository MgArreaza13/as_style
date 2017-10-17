import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.hostedcheckout.create_hosted_checkout_request import CreateHostedCheckoutRequest
from ingenico.connect.sdk.domain.hostedcheckout.definitions.hosted_checkout_specific_input import HostedCheckoutSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.customer import Customer
from ingenico.connect.sdk.domain.payment.definitions.order import Order

def Pago_Online(monto):
	configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),'./configuracion.ini'))
	api_key_id = os.getenv("connect.api.apiKeyId", "2028d86b7bc19213")
	secret_api_key = os.getenv("connect.api.secretApiKey", "bqz9C3UtR7MMO3zXL/v9uAwXSlnoUAXbn2wGbXeRo0w=")
	client = Factory.create_client_from_file(configuration_file_name=configuration_file_name,api_key_id=api_key_id, secret_api_key=secret_api_key)


	hosted_checkout_specific_input = HostedCheckoutSpecificInput()
	hosted_checkout_specific_input.locale = "en_GB"
	hosted_checkout_specific_input.variant = "testVariant"
	#hosted_checkout_specific_input.return_url = "http://multipoint.pythonanywhere.com/reservas/Procesar/Pago/Status/Retorno"

	amount_of_money = AmountOfMoney()
	amount_of_money.amount = monto*100
	amount_of_money.currency_code = "ARS"

	billing_address = Address()
	billing_address.country_code = "AR"

	customer = Customer()
	customer.billing_address = billing_address
	customer.merchant_customer_id = "Merchant 3738"

	order = Order()
	order.amount_of_money = amount_of_money
	order.customer = customer

	body = CreateHostedCheckoutRequest()
	body.hosted_checkout_specific_input = hosted_checkout_specific_input
	body.order = order



	response = client.merchant("3738").hostedcheckouts().create(body)
	print(response.__dict__)
	
	return response 
	 






def statusDePago(id):
	configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),'./configuracion.ini'))
	api_key_id = os.getenv("connect.api.apiKeyId", "2028d86b7bc19213")
	secret_api_key = os.getenv("connect.api.secretApiKey", "bqz9C3UtR7MMO3zXL/v9uAwXSlnoUAXbn2wGbXeRo0w=")
	client = Factory.create_client_from_file(configuration_file_name=configuration_file_name,api_key_id=api_key_id, secret_api_key=secret_api_key)

	response2 = client.merchant("3738").hostedcheckouts().get(id)
	print(response2.__dict__)
	return response2 


