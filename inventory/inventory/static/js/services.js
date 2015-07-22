var inventoryServices = angular.module('inventoryServices', ['ngResource']);

inventoryServices.factory('BaseItem', ['$resource',
  function($resource){
    return $resource('/apiv1/baseitems/?format=json', {}, {
      query: {method:'GET', isArray:true}
    })
  }
]);
