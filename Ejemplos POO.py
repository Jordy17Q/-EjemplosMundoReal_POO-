# archivo: taller_poo_completo.py

from abc import ABC, abstractmethod

# === ABSTRACCIÓN + ENCAPSULAMIENTO ===
class Dispositivo(ABC):
    def __init__(self, modelo, problema):
        self._modelo = modelo                  # Encapsulamiento: atributo privado
        self._problema = problema              # Encapsulamiento
        self._reparado = False                 # Encapsulamiento

    @abstractmethod
    def diagnosticar(self):
        pass

    def reparar(self):
        print(f"[Reparación] Reparando {self._modelo}...")
        self._reparado = True

    def estado(self):
        return "Reparado" if self._reparado else "Pendiente"

    def obtener_modelo(self):
        return self._modelo


# === HERENCIA ===
class Celular(Dispositivo):
    def __init__(self, modelo, problema, sistema_operativo):
        super().__init__(modelo, problema)
        self._sistema_operativo = sistema_operativo

    # === POLIMORFISMO: redefinimos 'diagnosticar' ===
    def diagnosticar(self):
        print(f"[Celular] {self._modelo} - Problema: {self._problema}")
        print(f"Sistema operativo: {self._sistema_operativo}")


class Laptop(Dispositivo):
    def __init__(self, modelo, problema, tiene_gpu_dedicada):
        super().__init__(modelo, problema)
        self._tiene_gpu_dedicada = tiene_gpu_dedicada

    # === POLIMORFISMO aplicado ===
    def diagnosticar(self):
        print(f"[Laptop] {self._modelo} - Problema: {self._problema}")
        gpu = "GPU dedicada" if self._tiene_gpu_dedicada else "GPU integrada"
        print(f"Configuración gráfica: {gpu}")


# === CLASE QUE INTERACTÚA CON LOS OBJETOS ===
class Taller:
    def __init__(self):
        self._inventario = []

    def ingresar_dispositivo(self, dispositivo: Dispositivo):
        self._inventario.append(dispositivo)
        print(f"[Ingreso] {dispositivo.obtener_modelo()} registrado en el sistema.")

    def diagnosticar_todos(self):
        for disp in self._inventario:
            disp.diagnosticar()

    def mostrar_estados(self):
        print("\n[Estado general de reparaciones]")
        for disp in self._inventario:
            print(f"{disp.obtener_modelo()}: {disp.estado()}")


# === EJEMPLO DE USO ===
if __name__ == "__main__":
    cel1 = Celular("Samsung A22", "No carga", "Android")
    lap1 = Laptop("HP Pavilion", "Pantalla sin imagen", True)

    taller = Taller()
    taller.ingresar_dispositivo(cel1)
    taller.ingresar_dispositivo(lap1)

    print("\n--- Diagnóstico ---")
    taller.diagnosticar_todos()

    print("\n--- Reparaciones ---")
    cel1.reparar()
    taller.mostrar_estados()