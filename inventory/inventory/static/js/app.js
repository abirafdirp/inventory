var inventoryApp = angular.module('inventory', [
  'ngRoute',
  'baseItemControllers',
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
      when('/dashboard', {
        templateUrl: '/dashboard/base-item-list',
        controller: 'BaseItemListCtrl'
      }).
      otherwise({
        redirectTo: '/dashboard'
      });
  }
]);