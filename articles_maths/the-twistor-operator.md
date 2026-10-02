
# __The Twistor Operator__

## Introduction

The covariant derivative of a spinor, $\nabla : \Gamma(\mathcal{S})\to\Gamma(T^*M\otimes\mathcal{S})$, is a first-order operator that depends on the metric used to define the spin connection; the Clifford contraction $c : T^*M\otimes\mathcal{S}\to\mathcal{S}$ is a bundle map whose kernel is a subbundle of the full tensor product, and projecting $\nabla$ onto that kernel produces a first-order operator that is **conformally invariant**. This operator is the **twistor operator**. It is the geometric operator that the conformal class of the metric, rather than the metric, defines, and its kernel consists of the **twistor spinors**, the spinor solutions of the twistor equation. On a four-dimensional conformal manifold the twistor operator is the analytic shadow of the twistor correspondence, and it is the first member of the family of conformally invariant first-order operators of the category.

The construction has three ingredients, each of which is an operator. The **Clifford multiplication** $c$ contracts a covector with a spinor, and it is a surjection with kernel $\ker c$; its adjoint $c^*$ embeds the spinors into the tensor product, and the composition $cc^*$ is the scalar $n$ on an $n$-manifold. The covariant derivative $\nabla$ therefore splits as the sum of a term with values in the image of $c^*$ — the part that carries the Cauchy–Riemann operator — and a term with values in $\ker c$, which is the twistor operator. This splitting is the orthogonal decomposition of $T^*M\otimes\mathcal{S}$ into $\ker c$ and $\operatorname{im}c^*$, and it is the reason the twistor operator is a projection of the familiar derivative rather than a new derivative.

**The boundaries.** The spin structure, the spinor bundle, the spin connection and the Cauchy–Riemann operator are *The Spinor Operator* and *Spin Geometry*; the Clifford multiplication as an operator is *The Clifford Multiplication Operator*; the adjoint of the twistor operator and the conformal equation are *The Adjoint of the Twistor Operator* and *The Penrose Operator*, written in parallel in this category. The twistor space, the twistor correspondence and the Penrose transform as complex-geometric objects are *Twistor Spaces and the Hermitian Structure of a Conformal Manifold* and *Hermitian Spin Geometry and the Twistor Correspondence*; only the differential-geometric operator is treated here, and the complex geometry is quoted. The conformal group and the conformal model of Euclidean space are *The Conformal Model of Euclidean Space* and *Conformal Geometry*. The base is a Riemannian spin manifold $(M,g)$ of dimension $n\ge3$, with $c(v)^2=-g(v,v)\operatorname{id}$ and $c(v)^*=-c(v)$.

## The Decomposition of the Covariant Derivative

### The Clifford Contraction and Its Kernel

**Definition.** The **Clifford contraction** is the bundle map induced by the Clifford multiplication,

$$
c : T^*M\otimes\mathcal{S}\longrightarrow\mathcal{S}, \qquad c(\xi\otimes\sigma) = \xi^{\sharp}\cdot\sigma ,
$$

where $\xi^{\sharp}$ is the tangent vector dual to $\xi$ under $g$ and the dot is the Clifford action. Its metric adjoint $c^* : \mathcal{S}\to T^*M\otimes\mathcal{S}$ is computed in a local orthonormal coframe $(\theta^1,\dots,\theta^n)$ by

$$
c^*\sigma = -\sum_{i=1}^{n}\theta^i\otimes(e_i\cdot\sigma), \qquad c(\xi\otimes\sigma) = \sum_i \xi(e_i)\,e_i\cdot\sigma .
$$

**Proposition.** The maps $c$ and $c^*$ are adjoint for the tensor product of $g$ and the fibre form $h$, $c$ is a surjection, and

$$
c\,c^* = n\,\operatorname{id}_{\mathcal{S}}, \qquad \ker c = \operatorname{im}c^* .
$$

Consequently $\pi = \operatorname{id} - \frac1n c^*c$ is the orthogonal projector of $T^*M\otimes\mathcal{S}$ onto $\ker c$, and $\frac1n c^*c$ is the projector onto $\operatorname{im}c^*$; the two subbundles are orthogonal complements and are both parallel only in the flat case.

**Proof.** Adjointness is the comparison of the two displays, using that the Clifford action by $e_i$ is skew-adjoint for $h$ and that the metric identifies $T^*M$ with $TM$; $c$ is surjective because $c(\xi\otimes(\xi\cdot\sigma)) = -g(\xi,\xi)\sigma$ for $\xi\ne0$. Then $cc^*\sigma = -\sum_ie_i\cdot(e_i\cdot\sigma)=\sum_i g(e_i,e_i)\sigma=n\sigma$. The identity $cc^*=n\operatorname{id}$ with $c$ surjective gives $\operatorname{im}c^*=(\ker c)^{\perp}$: for $\tau\in\ker c$, $h(c^*\sigma,\tau) = h(\sigma,c\tau)=0$, giving $\operatorname{im}c^*\subseteq(\ker c)^\perp$, and the dimensions agree because $c^*$ is injective (from $cc^*=n\operatorname{id}$). Hence $\pi$ is the orthogonal projector onto $\ker c$, and the two projectors sum to the identity. Both subbundles are parallel exactly when $\nabla$ preserves them, which in the flat case it does.

**Remark.** The number $n$ in $cc^*=n\operatorname{id}$ is the dimension of the manifold; it is the normalisation that makes $\pi$ a projection, and it is the reason the twistor operator has the constant $1/n$ in its definition.

### The Splitting and the Twistor Operator

**Definition.** The **twistor operator** is the composition of the covariant derivative with the projector onto the kernel of the Clifford contraction,

$$
\mathcal{T} = \pi\circ\nabla : \Gamma(\mathcal{S})\longrightarrow\Gamma(T^*M\otimes\mathcal{S}),
$$

equivalently, evaluated on a vector field $X$,

$$
\mathcal{T}_X\sigma = \nabla_X\sigma + \tfrac1n\,X\cdot D\sigma ,
$$

where $X\cdot$ is the Clifford multiplication and $D=c\circ\nabla$ is the Cauchy–Riemann operator of *The Spinor Operator*.

**Proposition (the splitting).** The covariant derivative decomposes as

$$
\nabla\sigma = \tfrac1n\,c^*\,D\sigma + \mathcal{T}\sigma ,
$$

the first term lying in $\operatorname{im}c^*$ and the second in $\ker c$; the two terms are the orthogonal components. Equivalently $c\circ\mathcal{T}=0$, and the part of $\nabla$ that is visible to the Clifford contraction is exactly the piece that carries $D$.

**Proof.** The definition gives $\mathcal{T}=\nabla-\tfrac1n c^*c\nabla$; and $c\nabla = D$ by definition of $D$, so $c^*c\nabla = c^*D$. Hence $\tfrac1n c^*c\nabla = \tfrac1n c^*D$ lies in $\operatorname{im}c^*$ and $\mathcal{T}\sigma$ lies in $\ker c$, because $c\mathcal{T}\sigma = c\nabla\sigma - \frac1n cc^*D\sigma = D\sigma - \frac1n n D\sigma = 0$. The two terms are orthogonal by the proposition above, and the decomposition is unique.

**Proposition (the symbol and the overdetermined ellipticity).** The principal symbol of $\mathcal{T}$ at a covector $\xi$ is

$$
\sigma_{\mathcal{T}}(x,\xi) = \pi\circ(\xi\otimes\,\cdot\,) : \mathcal{S}_x\longrightarrow\ker c_{\xi}\subseteq T_x^*M\otimes\mathcal{S}_x ,
$$

which is injective for $\xi\ne0$ and has image $\ker c_\xi$, of rank $(n-1)\dim\mathcal{S}$. The twistor operator is therefore overdetermined elliptic and not elliptic: its symbol is injective but not invertible.

**Proof.** The symbol is the highest-order part, computed by freezing the coefficient of $\mathcal{T}_X\sigma=\nabla_X\sigma+\frac1nX\cdot D\sigma$: the first term contributes $\xi(X)\sigma$ and the second $\frac1nX\cdot(\xi\cdot\sigma)$, whose sum over the frame is $\pi(\xi\otimes\sigma)$ by the computation of the symbol of $\pi$. If $\pi(\xi\otimes\sigma_0)=0$ then $\xi\otimes\sigma_0\in\operatorname{im}c^*$, so $\xi\otimes\sigma_0=-\frac1n c^*(\xi\cdot\sigma_0)$; applying $c$ gives $\xi\cdot\sigma_0 = -\frac1n n(\xi\cdot\sigma_0) = -\xi\cdot\sigma_0$, hence $\xi\cdot\sigma_0=0$ and then $\xi\otimes\sigma_0=0$, so either $\xi=0$ or $\sigma_0=0$. Thus the symbol is injective for $\xi\ne0$, and its image is $\pi(\mathcal{S})$ tensored with $\xi$, namely $\ker c_\xi$.

**Remark (why not elliptic, and why that is the point).** An injective but non-invertible symbol means that the twistor equation is an **overdetermined** system: it constrains the first derivatives, and its solutions are few. This is the analytic form of the geometric statement that a conformal structure singles out a special class of spinors, and it is the reason the twistor equation has a finite-dimensional solution space on a closed manifold in the conformally flat case, computed below.

## Conformal Invariance

### The Conformal Change of the Operator

**Given.** Two metrics $\hat g=\Omega^2g$ on $M$ with $\Omega>0$ have the same conformal class and hence the same frame bundle up to the scale; the spinor bundles are identified by the standard conformal rescaling of the spin module, and the identification is written $\sigma\mapsto\hat\sigma = \Omega^{-1/2}\sigma$ under the normalisation of the spinor form used in this corpus.

**Proposition (conformal covariance).** Let $\hat g=\Omega^2g$, $\Omega>0$, and let $X$ be a vector field, with $\hat X=\Omega^{-1}X$ its $\hat g$-dual counterpart. Then the twistor operator is conformally covariant,

$$
\mathcal{T}^{\hat g}_{\hat X}\bigl(\Omega^{-1/2}\sigma\bigr) = \Omega^{-1/2}\Bigl(\mathcal{T}^{g}_X\sigma\Bigr),
$$

so that the twistor equation $\mathcal{T}\sigma=0$ is conformally invariant: $\sigma$ is a twistor spinor for $g$ if and only if $\Omega^{-1/2}\sigma$ is a twistor spinor for $\hat g$.

**Proof sketch.** The conformal change of the Levi-Civita connection contributes the term $X\log\Omega$ to the spin connection, the change of the Clifford multiplication contributes the factor $\Omega$, and the change of the Cauchy–Riemann operator contributes its own zeroth-order term; the three contributions combine so that the correction terms to $\mathcal{T}$ cancel, which is the computation recorded by the references. The invariance of the zero set is the only consequence used below; the operator itself is covariant and not invariant because $\nabla$ and $D$ both change, and only their combination in $\mathcal{T}$ is stable.

**Remark (the contrast with the Cauchy–Riemann operator).** The Cauchy–Riemann operator is not conformally covariant: under a conformal change it acquires the zeroth-order term $c(\operatorname{grad}\log\Omega)$, as *The Spinor Operator* records. The twistor operator is exactly the part of the covariant derivative that is blind to that term, and this is the structural reason it exists: the conformal class, not the metric, defines the twistor equation, and the metric only defines the operator that projects onto it.

### The Twistor Equation

**Definition.** A spinor field $\sigma$ is a **twistor spinor**, or a conformal Killing spinor, when it lies in the kernel of the twistor operator,

$$
\nabla_X\sigma + \tfrac1n\,X\cdot D\sigma = 0 \qquad\text{for every vector field } X .
$$

The equation is the **twistor equation**; it is a first-order overdetermined system, conformally invariant by the proposition above.

**Proposition (the equivalent forms).** For a spinor field $\sigma$ the following are equivalent: (a) $\mathcal{T}\sigma=0$; (b) $\nabla_X\sigma=-\frac1n X\cdot D\sigma$ for every $X$; (c) the covariant derivative of $\sigma$ lies in $\operatorname{im}c^*$, equivalently $\nabla\sigma$ is a section of $\operatorname{im}c^*$; (d) there is a spinor field $\varphi$ with $\nabla_X\sigma = X\cdot\varphi$ for every $X$, and then $\varphi=-\frac1n D\sigma$ up to the kernel of the Clifford action.

**Proof.** (a) and (b) are the definition; (b) and (c) are the decomposition, because the component in $\ker c$ is exactly $\mathcal{T}\sigma$; (d) is the form (b) with $\varphi=-\frac1n D\sigma$, and conversely a field with $\nabla_X\sigma=X\cdot\varphi$ has $\nabla\sigma\in\operatorname{im}c^*$ because $X\cdot\varphi=c^*$ applied to a suitable element, so $\mathcal{T}\sigma=0$ and $\varphi$ is determined by $\sigma$ up to the kernel of the Clifford action.

**Remark (the name).** The name twistor spinor comes from the four-dimensional case, where the space of twistor spinors of the conformal structure is the space of holomorphic sections of the twistor space, and the operator is the analytic form of the twistor transform; this correspondence is *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*. The equation above is the differential-geometric statement, valid in every dimension $n\ge3$, and it is what the twistor correspondence generalises.

**Proposition (the flat and conformally flat solutions).** On the conformally flat model, the twistor equation has a solution space of dimension at most $2\dim\Delta_n$, and on simply connected conformally flat manifolds of dimension $n\ge3$ the bound is attained. The solutions are the twistor spinors of the conformal sphere, and they are the spinor-valued distributions of the conformal group: they carry a representation of the conformal Lie algebra generated by the translations, the rotations, the dilations and the special conformal transformations.

**Proof sketch.** The twistor equation is conformally invariant and the conformal group acts on the solution space, which is therefore a module over the conformal algebra; the bound is the algebraic statement that the first-order jet of a twistor spinor at a point is an element of $\mathcal{S}\oplus\ker c\subset\mathcal{S}\oplus(T^*\otimes\mathcal{S})$, of dimension $\dim\mathcal{S}+(n-1)\dim\mathcal{S}=n\dim\mathcal{S}$, and the conformal invariance propagates the jet; the comparison of $n\dim\Delta_n$ with $2\dim\Delta_n$ in low dimensions is the conformal representation theory quoted. The flat model $\hat g$ of the conformal sphere is the standard example computed below.

**Theorem (the Einstein case, quoted).** Let $(M,g)$ be a complete Einstein spin manifold and $\sigma$ a twistor spinor. Then $D\sigma$ is again a twistor spinor, the twistor operator and $D$ generate a finite-dimensional space of spinor fields, and on a complete Einstein manifold every twistor spinor is the sum of two Killing spinors; in particular, a twistor spinor on a Ricci-flat manifold is parallel.

**Proof sketch.** The twistor equation and its image under $D$ close into a system of ordinary differential equations along geodesics — the twistor equation is the parallel transport condition for a field built from $\sigma$ and $D\sigma$ — so the solution is determined by its jet at one point and the closure is a finite-dimensional argument; the decomposition into Killing spinors is the comparison of the two first-order equations $(\nabla_X\mp cX\cdot)\sigma=0$ that the twistor equation satisfies on an Einstein manifold with the appropriate Einstein constant. The result is quoted from the elliptic theory of the conformal operators.

## The Twistor Space

**Definition.** Let $(M,g)$ be a four-dimensional oriented Riemannian conformal manifold with spin structure, and $\mathcal{S}=\mathcal{S}^+\oplus\mathcal{S}^-$ the spinor bundle. The **twistor space** is the projectivised negative spinor bundle

$$
Z(M) = \mathbb{P}(\mathcal{S}^-) \longrightarrow M ,
$$

a bundle of projective lines with fibre $\mathbb{CP}^1$; a point of $Z(M)$ is a complex structure on the tangent space $T_xM$ compatible with $g$ and the orientation, and the fibre over $x$ is the sphere of such structures.

**Theorem (the twistor correspondence, quoted).** Let $(M,g)$ be an anti-self-dual four-dimensional conformal manifold with spin structure.

**(a)** The twistor space $Z(M)$ carries an integrable complex structure, and the projection $\pi : Z(M)\to M$ is holomorphic.

**(b)** Each point $x\in M$ determines a holomorphic rational curve $\pi^{-1}(x)\cong\mathbb{CP}^1$ in $Z(M)$, with normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$, and conversely such a curve determines a point of $M$.

**(c)** The conformal structure of $M$ is encoded in the complex structure of $Z(M)$ through the family of curves, and the twistor operator on $M$ is the differential operator whose kernel corresponds to the holomorphic sections of the appropriate bundle over $Z(M)$.

**Proof sketch.** The almost complex structure on $Z(M)$ is built from the horizontal lift of the Levi-Civita connection of any metric in the conformal class and the complex structure of the fibre, and its integrability is equivalent to the anti-self-duality of the Weyl curvature; the correspondence of curves and points is the theory of the twistor fibre with normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$, and the analytic statement identifying the twistor kernel with holomorphic sections is the Penrose transform, quoted from *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*. Only the two geometric statements (a) and (b) belong to the differential geometry of this article.

**Remark (the four-dimensional special position).** The twistor space is defined for a four-dimensional conformal manifold because the Hodge star acts on the two-forms and the Weyl curvature splits into self-dual and anti-self-dual parts; the choice of $\mathcal{S}^-$ rather than $\mathcal{S}$ is the choice of one of the two, and the integrability of the complex structure is exactly the vanishing of the anti-self-dual Weyl tensor. In the higher-dimensional case the analogue is the twistor space of the quaternionic Kähler geometry, which is *Quaternionic Geometry*; in dimension four the two constructions agree because $Sp(1)\cdot Sp(1)=SO(4)$.

## Worked Cases

### The Flat Conformal Model

On $\mathbb{R}^n$ with the Euclidean metric the twistor equation reads $\partial_X\sigma+\frac1nX\cdot\sum_ie_i\partial_i\sigma=0$. Taking $\sigma$ constant gives a twistor spinor with $D\sigma=0$; taking $\sigma(x)=x\cdot\eta$ for a constant spinor $\eta$ gives a twistor spinor with $D\sigma=-n\eta$, since $D(x\cdot\eta)=\sum_ie_i\partial_i(x\cdot\eta)=\sum_ie_ie_i\eta=-n\eta$. The space spanned by the constants and these linear fields is of dimension $2\dim\Delta_n$, attained in the flat model, and it is the representation of the conformal group by the twistor distribution.

### The Round Sphere

On the round sphere $S^n$ with its standard spin structure the metric is conformally flat and Einstein of positive scalar curvature; the twistor spinors are the pairs of Killing spinors with the two constants $\pm\frac12\sqrt{\frac{\operatorname{scal}}{n(n-1)}}$. The twistor equation restricts the differences of the two chiral twistors, of dimension $2\dim\Delta_n$, and the twistor space of $S^4$ with the round conformal structure is the complex projective space $\mathbb{CP}^3$ with its Fubini–Study structure: a Kodaira-type example of the correspondence where the twistor space is a projective space.

### The Einstein Manifolds

On a complete Einstein spin manifold with nonzero scalar curvature, the theorem above says that every twistor spinor is a sum of two Killing spinors with opposite constants, and on a Ricci-flat manifold every twistor spinor is parallel. The twistor operator therefore detects the Einstein condition: the existence of a twistor spinor that is not an eigenfield of $D$ is the failure of the Einstein equation, in the same way the existence of a Killing spinor detects the Einstein condition with the appropriate constant.

## Summary

The **Clifford contraction** $c : T^*M\otimes\mathcal{S}\to\mathcal{S}$ is the bundle map $\xi\otimes\sigma\mapsto\xi^{\sharp}\cdot\sigma$, a surjection whose adjoint $c^*$ satisfies $cc^*=n\operatorname{id}$ and whose kernel is $\ker c=\operatorname{im}c^*$ with the projector $\pi=\operatorname{id}-\frac1n c^*c$. The covariant derivative splits orthogonally as $\nabla\sigma=\frac1n c^*D\sigma+\mathcal{T}\sigma$, with $D=c\nabla$ the Cauchy–Riemann operator, and the second term is the **twistor operator** $\mathcal{T}\sigma=\nabla\sigma+\frac1n c(\cdot)\,D\sigma$; its symbol is $\pi(\xi\otimes\cdot)$, injective but not invertible, so the twistor operator is overdetermined elliptic and not elliptic. The twistor operator is **conformally covariant**, and the equation $\mathcal{T}\sigma=0$ is the **twistor equation**, whose solutions are the twistor spinors; on the conformally flat model the solution space has dimension $2\dim\Delta_n$, and on a complete Einstein manifold every twistor spinor is a sum of Killing spinors, parallel in the Ricci-flat case. On a four-dimensional anti-self-dual conformal manifold the twistor spinors correspond to holomorphic objects on the twistor space $Z(M)=\mathbb{P}(\mathcal{S}^-)$, and the correspondence is the twistor transform quoted from *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*. The adjoint of the twistor operator is *The Adjoint of the Twistor Operator*, and the conformally invariant form of the equation is *The Penrose Operator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{S}$, $c(v)$, $h$ | Spinor bundle, Clifford multiplication $c(v)^2=-g(v,v)$, fibre form |
| $c : T^*M\otimes\mathcal{S}\to\mathcal{S}$ | Clifford contraction, $c(\xi\otimes\sigma)=\xi^{\sharp}\cdot\sigma$ |
| $c^* : \mathcal{S}\to T^*M\otimes\mathcal{S}$ | Adjoint, $c^*\sigma=-\sum_i\theta^i\otimes(e_i\cdot\sigma)$ |
| $cc^*=n\operatorname{id}$, $\ker c=\operatorname{im}c^*$ | The trace identity and the orthogonal decomposition |
| $\pi=\operatorname{id}-\frac1nc^*c$ | Projector onto $\ker c$ |
| $D=c\circ\nabla$ | Cauchy–Riemann operator of the manifold |
| $\mathcal{T}=\pi\circ\nabla$, $\mathcal{T}_X\sigma=\nabla_X\sigma+\frac1nX\cdot D\sigma$ | Twistor operator |
| $\sigma_{\mathcal{T}}(\xi)=\pi\circ(\xi\otimes\cdot)$ | Symbol; injective, not invertible |
| $\mathcal{T}\sigma=0$ | Twistor equation; $\sigma$ a twistor spinor |
| $\hat g=\Omega^2g$ | Conformal change; $\mathcal{T}$ is conformally covariant |
| $Z(M)=\mathbb{P}(\mathcal{S}^-)$ | Twistor space of a four-dimensional conformal manifold |

## Further Reading

- Helga Baum, Thomas Friedrich, Ralf Grunewald and Ines Kath, *Twistors and Killing Spinors on Riemannian Manifolds* (Teubner, 1991), for the twistor operator, its conformal covariance and the twistor equation.
- Thomas Friedrich, *Dirac Operators in Riemannian Geometry* (American Mathematical Society, 2000), for the decomposition of the covariant derivative and the twistor and Killing spinor equations.
- Michael F. Atiyah, Nigel J. Hitchin and Isadore M. Singer, "Self-Duality in Four-Dimensional Riemannian Geometry", *Proceedings of the Royal Society of London A* 362 (1978), 425–461, for the twistor space of a four-dimensional conformal manifold and the twistor correspondence.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time, Volume 2* (Cambridge University Press, 1986), for the twistor equation, the conformal Killing spinors and the twistor transform.
- Simon Salamon, "Quaternionic Kähler Manifolds", *Inventiones Mathematicae* 67 (1982), 143–171, for the higher-dimensional twistor construction and its place in the category.
- Andrzej Trautman, "The Dirac Operator on Hypersurfaces", *Symposia Mathematica* 12 (1973), 139–151, for the conformal invariance of the twistor equation and the conformal Killing spinors.
