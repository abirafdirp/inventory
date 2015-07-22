var inventoryApp = angular.module('inventory', [
  'ngRoute',
  'inventoryControllers',
  'ui.bootstrap',
  'inventoryServices'
]);

inventoryApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

inventoryApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/base-item-list', {
        templateUrl: '/dashboard/base-item-list',
        controller: 'BaseItemListCtrl'
      }).
      when('/category-list', {
        templateUrl: '/dashboard/category-list',
        controller: 'CategoryListCtrl'
      }).
      otherwise({
        redirectTo: '/'
      });
  }
]);