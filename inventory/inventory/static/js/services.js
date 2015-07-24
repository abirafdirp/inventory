var inventoryServices = angular.module('inventoryServices', ['ngResource']);

inventoryServices.factory('BaseItem', ['$resource',
  function($resource){
    return $resource('/apiv1/baseitems/?format=json', {}, {
      query: {method:'GET'}
    })
  }
]);

inventoryServices.factory('Category', ['$resource',
  function($resource){
    return $resource('/apiv1/categories/?format=json', {}, {
      query: {method:'GET'}
    })

}]);

inventoryServices.factory('Item', ['$resource',
  function($resource) {
    return $resource('/apiv1/items/?format=json', {}, {
      query: {method:'GET'}
    })
  }
]);
