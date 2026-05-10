### Create a search service
```
Create an Azure AI Search service in the Azure portal
	Azure Portal
	Create a resource
	Find "Azure AI Search' -> Create
	Resource group: danny-search-service-resource-group
	Service name: dh-search-service
	Region: (US) East US 2
	Pricing tier: Basic
	Review + create
	Pricing tier
		Basic (15 GB/Partition, max 3 replicas, max 3 partitions, max 9 search units)
		Estimated cost per month $75.14
		Scale
		Replicas 1
		Partitions 1

	Create
	
	Url: https://dh-search-service.search.windows.net
	
```
https://learn.microsoft.com/en-us/azure/search/search-create-service-portal


### build and consume vector indexes 
```
Create and use a vector index for performing RAG in the Azure AI Foundry portal.
	Create an index from the Chat playground
	Azure AI Foundry -> Select Playgrounds -> Select the Chat Playground ->
	Set up - Deployment 
		Create new deployment -> From base models -> gpt-4.1-mini -> Confirm
		Or 
		Select the existing deployment
	
		Add your data - Add a data source -> Add data -> Select or add data source -> Select data source ->
		Upload files ->
			Select Azure Blob storage resource -> Create a new Azure Blob storage resource ->
			Resource group: danny-blob-resource-group 
			Storage account name: dannyblobaccount
			Region: (US) East US 2
			Primary service: Azure Blob Storage or ...
			Redundancy: Locally-redundant-storage (LRS)
			
			Review + create
			Create
			
			dannyblobaccount_1754242837214
		Select Azure Blob storage resource: dannyblobaccount
			Before enabling CORS, please ensure that you have created an Azure AI Search resource. 
			To create an Azure AI Search resource, please use the link below.
		Select Azure AI Search resource (free tier not supported)
			Create a new Azure AI Search resource (above)
		Enter the index name: dh_index_1
		
```

https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/index-add
