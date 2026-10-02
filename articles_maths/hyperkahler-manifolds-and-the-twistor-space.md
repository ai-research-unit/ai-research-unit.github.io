
# __Hyperkähler Manifolds and the Twistor Space__

## Introduction

A hyperkähler manifold carries three complex structures $J_1,J_2,J_3$ with the quaternionic relations, each a Kähler structure for the same metric. The three are not isolated: every unit quaternion $\lambda=ae_1+be_2+ce_3$ gives a complex structure

$$
I_\lambda = aJ_1+bJ_2+cJ_3 , \qquad I_\lambda^2=-\mathrm{id} ,
$$

and the whole family is a two-sphere, the **twistor family** of the manifold. The quaternionic conjugation $\lambda\mapsto\bar\lambda$ acts on the family by the antipode $I_\lambda\mapsto-I_\lambda$, and the pair $\{I_\lambda,I_{-\lambda}\}$ is the fibre over a point of the quotient sphere. The **twistor space** of the hyperkähler manifold is the total space of the family, and its complex structure makes the family a holomorphic fibration over $\mathbb{CP}^1$ with a holomorphic symplectic form on each fibre. This article treats the family, the twistor space, and the conjugation on both.

**The boundaries.** The hyperkähler structure, the forms $\omega_i$, the holonomy $Sp(n)$ and the hyperkähler quotient are *Hyperkähler Geometry*; the quaternionic structure and the conjugation on the structure bundle are *Quaternionic Geometry* and *Quaternionic Geometry and the Conjugate Structure*; the Kähler condition and the holomorphic symplectic form are *Kähler Geometry* and *Complex Manifolds*; the twistor space of a four-dimensional conformal manifold, its real structure and its Hermitian form are *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*, and the twistor operator is *The Twistor Operator*. The construction of the complex structure of the twistor space and the existence of the metrics on it use the elliptic methods of Part III and are cited. The base field is $\mathbb{R}$.

## The Twistor Family of Complex Structures

**Definition.** Let $(M,g,J_1,J_2,J_3)$ be hyperkähler with fundamental forms $\omega_i(X,Y)=g(J_iX,Y)$. For a unit imaginary quaternion $\lambda=ae_1+be_2+ce_3$, $a^2+b^2+c^2=1$, the **twistor family** is

$$
I_\lambda=aJ_1+bJ_2+cJ_3 , \qquad \Omega_\lambda = a\omega_1+b\omega_2+c\omega_3 .
$$

**Proposition.** For every unit $\lambda$ the endomorphism $I_\lambda$ is a complex structure compatible with $g$, $\Omega_\lambda$ is its fundamental form, $I_\lambda$ is parallel for the Levi-Civita connection, hence integrable, and $\Omega_\lambda$ is closed and Kähler for $g$; the assignment $\lambda\mapsto I_\lambda$ descends to a diffeomorphism from the sphere of unit imaginary quaternions modulo $\pm1$ onto a two-sphere of complex structures.

**Proof.** $I_\lambda^2=(a^2+b^2+c^2)(-\mathrm{id})=-\mathrm{id}$ by the quaternionic relations, and $I_\lambda$ is an isometry because each $J_i$ is; the compatibility of $\Omega_\lambda$ and its identification as the fundamental form are the bilinearity of $g$; the parallelness is the parallelness of the $J_i$, which is equivalent to the closedness of the $\omega_i$, and Novikov's theorem gives the integrability; the last statement is the bijectivity of the parametrisation modulo the sign.

**Theorem (the conjugation on the family, quoted).** The conjugation $\lambda\mapsto\bar\lambda$ of the quaternion algebra acts on the family by the antipode,

$$
I_{\bar\lambda}=I_{-\lambda}=-I_\lambda , \qquad \Omega_{\bar\lambda}=-\Omega_\lambda ,
$$

it is a free involution of the family, it reverses the orientation of the parameter sphere and hence acts on $\mathbb{CP}^1$ as an anti-holomorphic map without fixed points in the holomorphic parameter $\zeta\mapsto-\bar\zeta^{-1}$, and it is an isometry of the parameter sphere.

**Proof.** The conjugation negates the imaginary part, so $\bar\lambda=-\lambda$ for imaginary $\lambda$; the antipodal map of $S^2$ is free and orientation-reversing, and in the stereographic parameter it is $\zeta\mapsto-\bar\zeta^{-1}$, which is anti-holomorphic because it is the composite of the holomorphic $\zeta\mapsto-1/\zeta$ with the conjugation. The metric statement is the compatibility of the conjugation with the quaternionic norm.

**Remark (the sign in the forms).** The conjugation negates the complex structure and therefore negates its fundamental form, $\Omega_{\bar\lambda}=-\Omega_\lambda$; this is why the holomorphic symplectic form of the family, being of type $(2,0)$ for $I_\lambda$, is sent to the complex conjugate type for $I_{-\lambda}$ rather than to itself.

## The Twistor Space

**Definition.** The **twistor space** of the hyperkähler manifold is the total space of the twistor family,

$$
Z = M\times S^2 \quad\text{with the fibration}\quad \pi : Z\longrightarrow S^2=\mathbb{CP}^1 ,
$$

the fibre over $\lambda$ being $M$ with the complex structure $I_\lambda$; the **twistor lines** are the sections $x\mapsto (x,\lambda)$ for fixed $\lambda$, identified with $M$ as a complex manifold for that $\lambda$.

**Theorem (the complex structure, quoted).** The total space $Z$ carries a complex structure $I$ whose restriction to the fibre $\pi^{-1}(\lambda)$ is $I_\lambda$ and whose horizontal part is the family of the $I_\lambda$ transported across the sphere; with respect to it the fibration $\pi$ is holomorphic, the twistor lines are holomorphic sections with normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$, and on each fibre the two-form $\Omega_2+i\Omega_3$, restricted to the fibre $\pi^{-1}(e_1)$ and extended by the family, is a **holomorphic symplectic form** $\omega$ of $Z$: it is closed, of type $(2,0)$ with respect to $I$, and non-degenerate on the vertical tangent space.

**Proof sketch.** The integrability of $I$ uses the parallelness of the family and the holomorphicity of the fibration uses the anti-holomorphicity of the antipodal conjugation; the closedness of $\omega$ is that of the $\omega_i$ and the type is read from the Kähler forms of the family; the normal-bundle statement is the deformation computation of the twistor theory of *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*, quoted. The construction is the standard hyperkähler twistor construction and its details are the cited literature.

**Proposition (the compatibility with the four-dimensional case).** For a four-dimensional hyperkähler manifold the twistor space just defined agrees with the twistor space $\mathbb{P}(\mathcal{S}^-)$ of the conformal class, the twistor lines agree, and the real structure of the conformal twistor space restricts on each fibre to the antipodal map induced by the conjugation.

**Proof.** In dimension four a hyperkähler structure is the same datum as a self-dual conformal structure with a parallel spinor, so the projective spinor bundle is the bundle of compatible complex structures, the two fibrations have the same fibres and the same lines; the real structure is computed from the conjugation of the spinor bundle and coincides with the antipode on the fibres by the identification of *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*.

## The Conjugate Structure and the Reality Conditions

**Proposition.** The conjugation of the family is an isometric involution of $Z$ covering the antipodal map of the base sphere; it sends the fibre $M_\lambda$ to the conjugate complex manifold $M_{\lambda}$ with the opposite complex structure, it has no fixed point on the base, and its fixed points in $Z$ are the pairs of antipodal twistor lines; equivalently it maps the twistor space to the twistor space of the conjugate quaternionic structure of *Quaternionic Geometry and the Conjugate Structure*.

**Proof.** The conjugation acts on the base by the antipode, which is free, and on the fibre by the conjugation of the complex structure, which is the conjugate complex structure; the identification with the conjugate quaternionic structure is the definition of the latter; a fixed point would require a fixed point of the antipodal map, of which there is none.

**Corollary (the reality conditions).** A real structure on $Z$ in the sense of an anti-holomorphic involution compatible with the fibration is obtained by composing the conjugation of the family with an anti-linear involution of $M$; the hyperkähler manifolds with such an involution are the real hyperkähler manifolds, and their twistor spaces carry the reality conditions of the correspondence of *Twistor Spaces and the Hermitian Structure of a Conformal Manifold* on each fibre.

**Proof.** The composite is anti-linear on the fibres because the conjugation is anti-linear on the parameter and the extra involution may be taken anti-linear on $M$; the fibration is preserved because the antipode preserves the base; the reality statement is the restriction of the four-dimensional one.

## Worked Cases

### The Flat Quaternionic Space

For $\mathbb{H}^n$ with the flat metric the three structures are the constant left multiplications by $e_1,e_2,e_3$, the family $I_\lambda$ is constant in $\lambda$, and the twistor space is the product $\mathbb{H}^n\times\mathbb{CP}^1$ with the product complex structure; the holomorphic symplectic form is the constant form $\Omega_2+i\Omega_3$.

### The Four-Torus

For $T^4=\mathbb{H}/\Lambda$ the twistor family is the family of the flat Kähler structures of the same metric, and the twistor space is the product of the torus with the sphere; the twistor lines are the horizontal sections, and the conjugation pairs the two complex structures of each fibre.

### A $K3$ Surface

For a $K3$ surface with a hyperkähler metric the family is the full two-sphere of Kähler structures of the metric; the twistor space is a complex threefold with a holomorphic symplectic form, the twistor lines have normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$, and the conjugation acts by the antipode of the family, identifying the two orientations.

## Summary

A **hyperkähler manifold** carries the **twistor family** $I_\lambda=aJ_1+bJ_2+cJ_3$ of complex structures, indexed by the unit imaginary quaternions modulo sign, each compatible with the metric and Kähler with fundamental form $\Omega_\lambda$. The quaternionic conjugation acts on the family by the **antipode** $I_\lambda\mapsto-I_\lambda$, a free isometric involution, anti-holomorphic in the holomorphic parameter $\zeta\mapsto-\bar\zeta^{-1}$; it is the conjugation of the structure bundle of *Quaternionic Geometry and the Conjugate Structure*. The **twistor space** $Z=M\times S^2$ is the total space of the family, carrying a complex structure for which the fibration $Z\to\mathbb{CP}^1$ is holomorphic, the twistor lines are holomorphic with normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$, and a holomorphic symplectic form; in dimension four it agrees with the twistor space of the conformal class of *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*. The real structures of $Z$ are built from the conjugation and an anti-linear involution of $M$, and the flat space, the four-torus and a $K3$ surface are the worked cases.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J_1,J_2,J_3$ | Hyperkähler triple; $\omega_i(X,Y)=g(J_iX,Y)$ |
| $\lambda=ae_1+be_2+ce_3$ | Unit imaginary quaternion |
| $I_\lambda=aJ_1+bJ_2+cJ_3$ | Twistor family of complex structures |
| $\Omega_\lambda=a\omega_1+b\omega_2+c\omega_3$ | Fundamental form of $I_\lambda$ |
| $\lambda\mapsto\bar\lambda$ | Conjugation; acts by the antipode $I_\lambda\mapsto-I_\lambda$ |
| $\zeta\mapsto-\bar\zeta^{-1}$ | The conjugation in the holomorphic parameter |
| $Z=M\times S^2$, $\pi : Z\to\mathbb{CP}^1$ | Twistor space and its fibration |
| $\mathcal{O}(1)\oplus\mathcal{O}(1)$ | Normal bundle of a twistor line |
| $\omega=\Omega_2+i\Omega_3$ | Holomorphic symplectic form |

## Further Reading

- Nigel J. Hitchin, "The Self-Duality Equations on a Riemann Surface", *Proceedings of the London Mathematical Society* 55 (1987), 59–126, for the twistor family and the holomorphic symplectic form of a hyperkähler manifold.
- Simon Salamon, "Quaternionic Kähler Manifolds", *Inventiones Mathematicae* 67 (1982), 143–171, for the structure bundle $\mathcal{Q}$, the conjugation and the twistor fibration.
- Arthur L. Besse, *Einstein Manifolds* (Springer, 1987), for the hyperkähler manifolds, the holonomy $Sp(n)$ and the twistor constructions.
- Michael F. Atiyah, Nigel J. Hitchin and Isidore M. Singer, "Self-Duality in Four-Dimensional Riemannian Geometry", *Proceedings of the Royal Society of London A* 362 (1978), 425–461, for the four-dimensional twistor space and its real structure.
