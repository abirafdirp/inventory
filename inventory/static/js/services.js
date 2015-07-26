var inventoryServices = angular.module('inventoryServices', ['ngResource']);

inventoryServices.factory('BaseItem', ['$resource',
  function($resource){
    return $resource('/apiv1/baseitems/?format=json', {}, {
      query: {method:'GET', isArray:true}
    })
  }
]);

inventoryServices.factory('Category', ['$resource',
  function($resource){
    return $resource('/apiv1/categories/?format=json', {}, {
      query: {method:'GET', isArray:true}
    })

}]);

inventoryServices.factory('Brand', ['$resource',
  function($resource){
    return $resource('/apiv1/brands/?format=json', {}, {
      query: {method:'GET', isArray:true}
    })

}]);

inventoryServices.factory('Item', ['$resource',
  function($resource) {
    return $resource('/apiv1/items/?format=json', {}, {
      query: {method:'GET', isArray:true}
    })
  }
]);

inventoryServices.factory('Transaction', ['$resource',
  function($resource) {
    return $resource('/apiv1/transactions/?format=json', {}, {
      query: {method:'GET', isArray:true}
    })
  }
]);
inventoryServices.factory('Location', ['$resource',
  function($resource) {
    return $resource('/apiv1/locations/?format=json', {}, {
      query: {method:'GET', isArray:true}
    })
  }
]);
inventoryServices.factory('ItemsInLocations', ['$resource',
  function($resource) {
    return $resource('/apiv1/items-in-locations/?format=json', {}, {
      query: {method:'GET', isArray:true}
    })
  }
]);
