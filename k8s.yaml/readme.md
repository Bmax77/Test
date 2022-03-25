kind: DeploymentConfig
...
          volumeMounts:
            - name: volume-k5dem
              mountPath: /etc/prometheus
      volumes:
        - name: volume-k5dem
          configMap:
            name: prometheus-config
            defaultMode: 420


---
kind: ConfigMap
apiVersion: v1
metadata:
  name: prometheus-config
  namespace: ci01978215-ipromgen-hr-platform-os4-alpha-prom
data:
  prometheus.yml: |-
    global:
      scrape_interval: 10s
      scrape_timeout: 10s
      evaluation_interval: 10s