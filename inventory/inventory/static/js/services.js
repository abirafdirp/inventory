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

inventoryServices.factory('Brand', ['$resource',
  function($resource){
    return $resource('/apiv1/brands/?format=json', {}, {
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

inventoryServices.factory('Transaction', ['$resource',
  function($resource) {
    return $resource('/apiv1/transactions/?format=json', {}, {
      query: {method:'GET'}
    })
  }
]);
inventoryServices.factory('IsFormSubmitted', function() {
  var submitted;
  function set(data) {
    submitted = data;
  }
  function get() {
    return submitted;
  }
  return {
    set: set,
    get: get
  }
});
