# __Hermitian Connections and the Adjoint__

## Introduction

A connection on a vector bundle may be **transposed** to the dual bundle and **conjugated** on the conjugate bundle, and a Hermitian metric identifies the two operations: the metric-compatible connections are exactly the connections whose dual and whose conjugate agree under the metric. This is the **self-adjointness** of the connection, and it is the reason that a metric connection has a skew-Hermitian curvature and that the covariant derivative has the simple adjoint $-\nabla_X-\operatorname{div}X$.

The article develops the adjoint connection. It defines the dual connection $\nabla^*$ on $E^*$ by the derivative of the pairing and the conjugate connection $\bar\nabla$ on $\bar E$, proves that the Hermitian metric is a conjugate-linear isomorphism intertwining them exactly when the connection is metric-compatible, computes the **adjoint of a single covariant derivative** $\nabla_X$ as a differential operator, identifies the **connection Laplacian** $\nabla^*\nabla$ as the composition with the formal adjoint at the level of the $1$-form-valued sections, and computes the **curvature of the adjoint connection** $R_{\nabla^*}(X,Y)=-R_\nabla(X,Y)^t$, deriving again that the curvature of a metric connection is skew-Hermitian.

The article assumes the connections, the connection form, the curvature and the change of the structure group of *Fibre Bundles, Connections and Curvature*; the covariant derivative, metric compatibility, the torsion and the curvature as an operator of *The Covariant Derivative*, in this category; the Hermitian metrics, the conjugate bundle and the isomorphism $\flat:\bar E\to E^*$ and the skew-Hermitian curvature of a metric connection of *Hermitian Vector Bundles and the Chern Connection*; the formal adjoint, the density correction and the pairing of *The Formal Adjoint of a Differential Operator*, the previous entry of this group; and the Hodge star, the codifferential and the divergence of *The Exterior Derivative* and *The Codifferential*. The global $L^2$ adjoint of the connection Laplacian and its domain are *The L2 Adjoint of a Differential Operator*, the next entry. The Atiyah–Singer and index-theoretic uses of the connection Laplacian are *Dirac Differential Operators* and *The Atiyah–Singer Index Theorem and K-Theory* in this Part. No physics is invoked.

## The Dual and the Conjugate Connection

### The Dual Connection

**Definition.** Let $\nabla$ be a connection on $E$ and let $\langle\cdot,\cdot\rangle : E^*\times E \to \mathbb{C}$ be the pairing. The **dual connection** $\nabla^*$ on $E^*$ is defined by the Leibniz rule

$$
d\langle\xi, s\rangle = \langle\nabla^*\xi, s\rangle + \langle\xi, \nabla s\rangle, \qquad \xi \in \Gamma(E^*), \ s \in \Gamma(E).
$$

**Proposition.** The dual connection is a connection; in a frame, if $\nabla = d+\omega$ with connection form $\omega$, then $\nabla^* = d - \omega^{T}$, so the connection form of the dual is the negative transpose. The dual of the dual is the original, $(\nabla^*)^* = \nabla$, and the passage to the dual is compatible with the composition of connections: $(E\otimes F)^* = E^*\otimes F^*$ and the dual of a tensor-product connection is the tensor product of the duals.

*Proof.* Read the defining rule on sections $\xi = \sum_i\xi_i e^i$ in the dual frame of a frame $e_i$ with $\nabla e_j = \sum_i\omega^i_j\,e_i$. Then $d\langle\xi,e_j\rangle = d\xi_j$ and $\langle\xi,\nabla e_j\rangle = \sum_i\omega^i_j\xi_i$, so $\langle\nabla^*\xi,e_j\rangle = d\xi_j - \sum_i\omega^i_j\xi_i = \sum_i(d\xi_i - \sum_j\omega^i_j\xi_j)\delta_{ij}$, giving the negative transpose in the dual frame; the assertions about the double dual and the tensor product follow from the same computation.

**Example.** The Levi-Civita connection on $TM$ and its dual on $T^*M$; the covariant derivative of a $1$-form is the dual of the covariant derivative of a vector field, and the two are computed by the same Christoffel symbols with the contraction. For the trivial line bundle with the trivial connection on the functions, the dual connection is the exterior derivative on the $1$-forms read as the dual sections, since $d\langle\xi,s\rangle=\langle d\xi,s\rangle$ for a function $s$.

### The Conjugate Connection

**Definition.** Let $\bar E$ be the conjugate bundle, with the same underlying real bundle and the opposite complex structure, $\lambda\cdot_{\bar E}s = \bar\lambda\,s$, as in *Hermitian Vector Bundles and the Chern Connection*. A connection $\nabla$ on $E$ induces a connection $\bar\nabla$ on $\bar E$ by the same real formula; in frames, if $\nabla = d+\omega$, then $\bar\nabla = d+\bar\omega$, the conjugate of the connection form.

**Proposition.** The conjugate connection is a connection; it is $\mathbb{C}$-antilinear in the sense that the same real operator acts on the two bundles, and on the complexified tensor powers $E^{\otimes p}\otimes\bar E^{\otimes q}$ the induced connection has the connection form with $p$ copies of $\omega$ and $q$ copies of $\bar\omega$.

*Proof.* The conjugate bundle carries the same real structure, so the same real connection is well defined on it; the statement on the frames is the computation of the connection form on the conjugate bundle, whose transition functions are the conjugates of those of $E$, so the connection form conjugates. The tensor-power statement is the functoriality of the connection.

## Metric Compatibility as Self-Adjointness

**Theorem (the self-adjointness of a metric connection).** Let $h$ be a Hermitian metric on $E$ and let $\flat : \bar E \to E^*$ be the conjugate-linear isomorphism $s\mapsto h(s,\cdot)$. Then $\nabla$ is metric-compatible if and only if $\flat$ is **parallel** for the pair $(\nabla,\nabla^*)$:

$$
\nabla^*\circ\flat = \flat\circ\nabla, \qquad \text{as operators } \Gamma(E)\to\Omega^1(M;E^*),
$$

where $\nabla$ acts on the $E$-valued (or $1$-form-valued) sections through the underlying real structure of $\bar E$ and $\flat$ acts on the values; equivalently, the measurement of the connection by the metric is self-adjoint:

$$
d\,h(s,t) = \bigl(\nabla^*\flat(s)\bigr)(t) + h(s,\nabla t) = h(\nabla s, t)+h(s,\nabla t).
$$

*Proof.* Evaluate the intertwining identity on sections $s$ and $t$, using the definition of the dual connection with the pairing $\langle\flat(s),t\rangle = h(s,t)$: the identity reads $\langle\nabla^*\flat(s),t\rangle = h(\nabla s,t)$; the defining rule of the dual connection writes the left side as $dh(s,t)-h(s,\nabla t)$. Comparing with the right side gives $dh(s,t) = h(\nabla s,t)+h(s,\nabla t)$, the metric-compatibility equation, and the computation reverses. In frames, with $H$ the metric matrix and $\omega$ the connection form, the identity is the matrix equation $dH = \bar\omega^{T}H+H\omega$, which is the metric-compatibility equation of *Hermitian Vector Bundles and the Chern Connection*.

**Corollary.** A metric connection $\nabla$ is self-adjoint under the metric $\flat$: the connection form on $E\oplus E^*$ is $h$-skew-Hermitian in the sense that the difference of two metric connections is $h$-anti-Hermitian, and the operator $\nabla\oplus\nabla^*$ is formally self-adjoint for the pairing extended by $h$.

*Proof.* The intertwining identity shows that $\nabla$ on $E$ is transported by $\flat$ to $\nabla^*$ on $E^*$; the block form follows by writing the connection on $E\oplus E^*$ as the direct sum and using the anti-Hermitian difference of two metric connections, as in the previous group.

## The Adjoint of a Covariant Derivative

### The Formal Adjoint of $\nabla_X$

Let the manifold carry a density $d\mu$, as in *The Formal Adjoint of a Differential Operator*, and let the sections be paired by $\langle s,t\rangle_{L^2}=\int_M h(s,t)\,d\mu$.

**Theorem.** For a metric-compatible connection $\nabla$ and a vector field $X$,

$$
(\nabla_X)^* = -\nabla_X - \operatorname{div} X,
$$

acting as a differential operator on the sections, where the divergence is taken with respect to the density; consequently $\nabla_X$ is skew-adjoint exactly when $\operatorname{div}X = 0$.

*Proof.* Compute with the metric-compatibility identity and the metric nature of the pairing. For the pairing with compact support $\int_M X\,h(s,t)\,d\mu = \int_M h(\nabla_Xs,t)\,d\mu + \int_M h(s,\nabla_Xt)\,d\mu$, and by the integration by parts of the previous entry $\int_M X\,f\,d\mu = -\int_M f\,\operatorname{div}X\,d\mu$ for a function $f$. Substituting and collecting the two terms in $h(s,\cdot)$ gives $\int_M h(\nabla_Xs,t)\,d\mu = -\int_M h(s,\nabla_Xt + \operatorname{div}X\,t)\,d\mu$, which is the display.

**Remark.** The formula exhibits the self-adjointness of the metric connection up to the divergence of the direction field: the adjoint of $\nabla_X$ is the negative of the covariant derivative along $X$ with the density correction, and the correction vanishes exactly for the divergence-free fields. The skew-adjointness of the differential $d$ and the first-order part of the Dirac operator, as in *Dirac Differential Operators* and *The Atiyah–Singer Index Theorem and K-Theory*, are instances of this formula with the appropriate density.

### The Connection Laplacian

**Definition.** The **connection Laplacian** (or Bochner Laplacian) of a metric connection is the operator on the sections

$$
\nabla^*\nabla s = -\sum_i \bigl(\nabla_{e_i}\nabla_{e_i}s - \nabla_{\nabla_{e_i}e_i}s\bigr),
$$

where $e_1,\ldots,e_n$ is a local orthonormal frame, $\nabla^* : \Gamma(T^*M\otimes E)\to\Gamma(E)$ is the formal adjoint of $\nabla : \Gamma(E)\to\Gamma(T^*M\otimes E)$ read as the contraction $\nabla^* = -\operatorname{tr}_g\nabla$, and the display is up to the sign convention of the Laplace operator; the second term with the divergence of the frame is what makes the expression coordinate-free.

**Proposition.** The connection Laplacian is a formally self-adjoint second-order operator; its principal symbol is $\lvert\xi\rvert^2\,\mathrm{id}$, so it is elliptic and positive semidefinite; for the trivial connection on functions it is the Laplace–Beltrami operator, and for the Levi-Civita connection on the tangent bundle it is the rough Laplacian of the metric.

*Proof.* The formal self-adjointness is $\langle\nabla^*\nabla s,t\rangle_{L^2} = \langle\nabla s,\nabla t\rangle_{L^2} = \langle s,\nabla^*\nabla t\rangle_{L^2}$ up to the sign, which is the pairing of the $1$-form-valued sections by the metric extended to $T^*M\otimes E$; the symbol is computed from the second-order part, which is the metric contraction, $-\sum g^{ij}\partial_i\partial_j$, whose symbol is $g^{ij}\xi_i\xi_j=\lvert\xi\rvert^2$. The identifications with the Laplace–Beltrami and the rough Laplacian are the definitions.

## The Curvature of the Adjoint Connection

**Theorem.** The curvature of the dual connection is the negative transpose of the curvature of $\nabla$,

$$
R_{\nabla^*}(X,Y) = -\,R_\nabla(X,Y)^{t}, \qquad \text{in frames} \ \Omega_{\nabla^*} = -\,\Omega_\nabla^{\,T},
$$

and the curvature of the conjugate connection is the conjugate, $R_{\bar\nabla}(X,Y)=\overline{R_\nabla(X,Y)}$. Consequently, for a metric-compatible connection, the curvature is skew-Hermitian with respect to the metric,

$$
R_\nabla(X,Y)^* = -R_\nabla(X,Y), \qquad \text{equivalently} \ \Omega_\nabla^*=-\Omega_\nabla,
$$

where $^*$ is the adjoint with respect to $h$; this is the skew-Hermitian curvature of the previous group, derived here from the adjointness.

*Proof.* The curvature is the commutator of the covariant derivatives, $R(X,Y)=\nabla_X\nabla_Y-\nabla_Y\nabla_X-\nabla_{[X,Y]}$, and the passage to the dual and to the conjugate is a functor sending the composition to the composition and the commutator to the commutator; hence the curvature of the dual is the transpose of the commutator with the signs reversed, and the curvature of the conjugate is the conjugate of the commutator. For the metric-compatible case, transporting the curvature identity through the intertwining identity $\nabla^*\circ\flat=\flat\circ\nabla$ relates the transpose of $\Omega$ to $\Omega$ through the metric $H$, and the metric-compatibility equation $dH=\bar\omega^TH+H\omega$ turns this into the skew-Hermitian condition $\Omega^*H+H\Omega=0$, which is the same computation as in *Hermitian Vector Bundles and the Chern Connection*.

**Corollary.** A connection and its dual have the same characteristic class; the transposition and the conjugation fix the Chern classes and multiply the symplectic and the real characteristic classes according to the degree, as in *Chern Classes of a Hermitian Bundle* and *Characteristic Classes*.

## Summary

A connection has a **dual** on $E^*$, with connection form the negative transpose, and a **conjugate** on the conjugate bundle, with connection form the conjugate; the Hermitian metric is a conjugate-linear isomorphism $\flat:\bar E\to E^*$ that links the two. The connection is **metric-compatible** exactly when $\flat$ intertwines the connection with its dual, which is the self-adjointness of the connection; the operator $\nabla\oplus\nabla^*$ is then self-adjoint and its connection form is $h$-skew-Hermitian. The adjoint of a single covariant derivative is $(\nabla_X)^*=-\nabla_X-\operatorname{div}X$, a differential operator, and the connection Laplacian $\nabla^*\nabla$ is self-adjoint, elliptic and nonnegative, reducing to the Laplace–Beltrami operator on functions. The curvature of the dual is the negative transpose and the curvature of the conjugate is the conjugate; for a metric connection the curvature is skew-Hermitian, which is the origin of the real Chern forms of the Hermitian bundle.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| Pairing $\langle\xi,s\rangle$ on $E^*\times E$ | The fibrewise pairing of the dual and the bundle |
| Dual connection $\nabla^*$ | $d\langle\xi,s\rangle=\langle\nabla^*\xi,s\rangle+\langle\xi,\nabla s\rangle$; $\nabla^*=d-\omega^T$ |
| Conjugate bundle $\bar E$, conjugate connection $\bar\nabla$ | Opposite complex structure; $\bar\nabla=d+\bar\omega$ |
| $\flat : \bar E\to E^*$, $s\mapsto h(s,\cdot)$ | The conjugate-linear isomorphism of the metric |
| $\flat\circ\bar\nabla=\nabla^*\circ\flat$ | Metric compatibility; self-adjointness of the connection |
| $(\nabla_X)^*=-\nabla_X-\operatorname{div}X$ | Adjoint of a covariant derivative |
| $\nabla^*\nabla$, connection Laplacian | Self-adjoint, elliptic, symbol $\lvert\xi\rvert^2\,\mathrm{id}$ |
| $R_{\nabla^*}(X,Y)=-R_\nabla(X,Y)^t$ | Curvature of the dual |
| $R_{\bar\nabla}=\overline{R_\nabla}$, $\Omega^*=-\Omega$ | Curvature of the conjugate; skew-Hermitian curvature |
| $\nabla\oplus\nabla^*$ | Self-adjoint operator on $E\oplus E^*$ |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, vol. I (Interscience, 1963), for the dual connection, the conjugate connection and the curvature of a metric connection.
- Nicole Berline, Ezra Getzler and Michèle Vergne, *Heat Kernels and Dirac Operators* (Springer, 1992), for the connection Laplacian, its self-adjointness and the Weitzenböck formulas.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the adjoint of the covariant derivative, the connection Laplacian and the Dirac operators.
- John M. Lee, *Riemannian Manifolds: An Introduction to Curvature* (Springer, 1997), for the divergence, the rough Laplacian and the integration by parts on a Riemannian manifold.
- Michael E. Taylor, *Partial Differential Equations*, vol. I (Springer, 2nd ed. 2011), for the self-adjointness of the connection Laplacian and its domain, cited for the forward reference.
