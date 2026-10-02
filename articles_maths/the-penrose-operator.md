
# __The Penrose Operator__

## Introduction

The **Penrose operator** is the conformally invariant first-order operator on spinors whose kernel is the space of twistor spinors. It is the twistor operator of *The Twistor Operator*, read from the side of the equation: where that article computes the symbol and the splitting of the covariant derivative, this article treats the conformal weights, the invariances, and the conformal fields that a twistor spinor produces. The twistor equation

$$
\nabla_X\sigma + \tfrac1n\,X\cdot D\sigma = 0
$$

is the equation of the operator; its solutions are the twistor spinors, or conformal Killing spinors, and the operator's defining property is that the equation depends on the conformal class of the metric and not on the metric. The operator is named after the conformally invariant form of the twistor programme, where the same first-order equation controls the analytic objects attached to the twistor space.

The content of the article is the conformal structure of the equation. The twistor equation is a first-order system that is not elliptic but overdetermined; its solutions on the conformally flat model are the spinor-valued distributions of the conformal group, of dimension $2\dim\Delta_n$; on a closed Einstein manifold they are the sums of Killing spinors; and a twistor spinor pairs with its conjugate to give a conformal Killing field, which is the real-geometry bridge between the spinor data and the conformal group. Each of these statements is a conformal statement, and the reason the operator exists is that the Cauchy–Riemann operator of *The Spinor Operator* is not conformally covariant: it acquires a zeroth-order term, and the twistor operator is the part of the covariant derivative that does not.

**The boundaries.** The operator, its symbol and the decomposition of the covariant derivative are *The Twistor Operator*; the Cauchy–Riemann operator and the spin connection are *The Spinor Operator*; the Clifford multiplication is *The Clifford Multiplication Operator*; the conformal group, the conformal model of Euclidean space and the conformal invariance of the operators of this part are *Conformal Geometry* and *The Conformal Model of Euclidean Space*. The Killing spinor equation and its relation to the Einstein condition are *Spin Geometry* and *Killing Spinors and the Einstein Condition*; the twistor space and the Penrose transform as complex geometry are *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*. The base is a Riemannian spin manifold $(M,g)$ of dimension $n\ge3$ with $c(v)^2=-g(v,v)\operatorname{id}$; the two-dimensional case, where the weights degenerate, is indicated.

## The Operator and the Equation

### Definition

**Definition.** The **Penrose operator** is the first-order differential operator

$$
\mathcal{P}_X\sigma = \nabla_X\sigma + \tfrac1n\,X\cdot D\sigma , \qquad X\in TM,\ \sigma\in\Gamma(\mathcal{S}),
$$

where $D=c\circ\nabla^{\mathcal{S}}$ is the Cauchy–Riemann operator. As a map it takes a spinor field to a tangent-valued spinor field, $\mathcal{P} : \Gamma(\mathcal{S})\to\Gamma(T^*M\otimes\mathcal{S})$, and its kernel consists of the **twistor spinors**.

**Proposition.** The Penrose operator is the twistor operator of *The Twistor Operator*: $\mathcal{P}=\pi\circ\nabla^{\mathcal{S}}$ with $\pi=\operatorname{id}-\frac1n c^*c$ the orthogonal projector onto the kernel of the Clifford contraction. Its principal symbol is injective with image $\ker c_{\xi}$, and it is overdetermined elliptic. The display is the same operator written with the index $X$ exposed.

**Proof.** The identity $\mathcal{P}_X\sigma=\nabla_X\sigma+\frac1nX\cdot D\sigma$ is the definition, and it coincides with $(\pi\nabla^{\mathcal{S}}\sigma)(X)$ by the computation of the splitting in *The Twistor Operator*; the symbol statement is proved there and is recorded here for completeness.

**Remark (why two names).** The same operator is called the twistor operator when one thinks of the mapping properties and the symbol, and the Penrose operator when one thinks of the equation and its conformal invariance. The corpus keeps both names, with the division of labour above; no second operator is introduced.

### The Twistor Equation and Killing Spinors

**Definition.** A spinor field $\sigma$ with $\mathcal{P}\sigma=0$ is a **twistor spinor**; the equation is the **twistor equation**. A spinor field satisfying $\nabla_X\sigma=\lambda\,X\cdot\sigma$ for a constant $\lambda$ is a **Killing spinor** with constant $\lambda$.

**Proposition.** A Killing spinor with constant $\lambda$ is a twistor spinor, and $D\sigma=-n\lambda\sigma$ for it; conversely, a twistor spinor with $D\sigma=-n\lambda\sigma$ and $\lambda$ constant is a Killing spinor.

**Proof.** If $\nabla_X\sigma=\lambda X\cdot\sigma$ then $D\sigma=\sum_ie_i\cdot\nabla_{e_i}\sigma=\lambda\sum_ie_i\cdot e_i\cdot\sigma=-n\lambda\sigma$, so $\frac1n X\cdot D\sigma=-\lambda X\cdot\sigma$ and the twistor equation holds. Conversely, a twistor spinor with $D\sigma=-n\lambda\sigma$ has $\nabla_X\sigma=-\frac1nX\cdot D\sigma=\lambda X\cdot\sigma$.

**Remark.** The Killing spinors are the twistor spinors whose Cauchy–Riemann eigenvalue is the compatible constant; on the round sphere the twistor spinors are exactly the sums of the two families of Killing spinors with constants $\pm\frac12\sqrt{\frac{\operatorname{scal}}{n(n-1)}}$, which is the statement of *The Twistor Operator* in the Einstein case.

### Conformal Covariance

**Theorem (conformal invariance of the twistor equation).** Let $\hat g=\Omega^2g$ with $\Omega>0$, and identify the spinor bundles of $g$ and $\hat g$ along the conformal factor in the standard way, writing $\hat\sigma$ for the image of a spinor field $\sigma$. Then the twistor equation is conformally invariant:

$$
\mathcal{P}^{g}\sigma = 0 \qquad\Longleftrightarrow\qquad \mathcal{P}^{\hat g}\hat\sigma = 0 ,
$$

with the weight fixed by the standard identification. In particular the space of twistor spinors is an invariant of the conformal class $[g]$, and the Penrose operator is the conformally covariant operator that realises the invariance.

**Proof sketch.** The conformal change of the spin connection contributes the term $(X\log\Omega)$-valued Clifford multiplication to $\nabla^{\mathcal{S}}$, and the change of the Cauchy–Riemann operator contributes its own first-order and zeroth-order corrections; the combination defining $\mathcal{P}$ is the unique such combination whose corrections cancel, which is the computation recorded by the references and quoted here. The cancellation is the conformal form of the statement that the two terms of $\mathcal{P}$ — the trace part and the twistor part of $\nabla^{\mathcal{S}}$ — carry opposite conformal weights.

**Remark (where the weight sits).** The operator is not conformally invariant as a map between the same bundles; it is covariant, and the invariance statement is the invariance of its zero set under the weighted identification. This is the same state of affairs as for the conformal Laplacian of conformal geometry: the geometric object is the equation, and the operator depends on the representative metric.

## Conformal Fields from Twistor Spinors

### The Conformal Current

**Proposition (the conformal Killing field).** Let $\sigma$ be a twistor spinor. Then the vector field

$$
X_\sigma = \sum_{i=1}^{n}\bigl(\sigma,e_i\cdot\sigma\bigr)\,e_i ,
$$

where $(\cdot,\cdot)$ is the real part of the fibre form, is a **conformal Killing field**: it satisfies the conformal Killing equation

$$
\mathcal{L}_{X_\sigma}g = \frac{2}{n}(\operatorname{div}X_\sigma)\,g .
$$

Equivalently, the flow of $X_\sigma$ preserves the conformal class of $g$.

**Proof sketch.** The twistor equation for $\sigma$ gives a first-order system for the vector field $X_\sigma$; differentiating the defining formula and substituting $\nabla_X\sigma=-\frac1nX\cdot D\sigma$ shows that the symmetric part of $\nabla X_\sigma$ is a multiple of the metric, which is the conformal Killing equation, and the divergence is computed from the same formula. This is the standard construction of the conformal vector fields adapted to a spinor, quoted from the theory of twistor spinors; it is the real-geometry face of the twistor equation.

**Remark.** The current $X_\sigma$ is bilinear once two twistor spinors are used, $X_{\sigma,\tau}=\sum_i(\sigma,e_i\cdot\tau)e_i$; the pairing of the twistor spinors therefore produces the conformal algebra, and on the conformally flat model the twistor spinors are the spinor-valued realisation of the conformal group. This is the bridge from the operator to *Conformal Geometry*.

### The Solution Space

**Proposition (the flat model dimension).** On the conformally flat model of dimension $n\ge3$ the space of twistor spinors has dimension $2\dim\Delta_n$, where $\Delta_n$ is the spin module; it is the spinor-valued representation of the conformal Lie algebra $\mathfrak{so}(n+1,1)$ generated by the translations, the rotations, the dilations and the special conformal transformations.

**Proof sketch.** A twistor spinor is determined by its one-jet at a point, which lies in $\mathcal{S}\oplus\ker c$ of dimension $n\dim\mathcal{S}$ by the symbol computation; the conformal invariance propagates the jet along the conformal geodesics, and the algebra acts on the solution space, which is therefore a module over the conformal algebra. Its dimension in the flat model is $2\dim\Delta_n$, as computed for the conformal sphere; the representation-theoretic identification is quoted. The flat twistor spinors are the constants and the linear fields of *The Twistor Operator*.

**Theorem (the Einstein case, quoted).** On a complete Einstein spin manifold every twistor spinor is the sum of two Killing spinors, and on a Ricci-flat manifold every twistor spinor is parallel.

**Proof sketch.** The twistor equation on an Einstein manifold closes with its image under $D$ into a parallel-transport system of finite rank, presented in *The Twistor Operator*; the closure forces the two eigenfields of $D$ in the spanned space to be Killing, with the two constants determined by the Einstein constant.

## Worked Cases

### The Conformal Sphere

On $S^n$ with the round metric the twistor spinors are the sums of the two Killing families, and the conformal group $O(n+1,1)$ acts on the $2\dim\Delta_n$-dimensional space. The conformal compactification of $\mathbb{R}^n$ is $S^n$ with the round metric, and the flat twistor spinors of $\mathbb{R}^n$ extend to the sphere; the extension is the conformal invariance of the equation made concrete.

### The Flat Conformal Model

On $\mathbb{R}^n$ with the Euclidean metric the Penrose operator has the solutions $\sigma=$ constant and $\sigma(x)=x\cdot\eta$ for constant $\eta$; the first has $D\sigma=0$ and the second $D\sigma=-n\eta$, so both are twistor spinors with the appropriate Cauchy–Riemann eigenvalues, and the constants and the linear fields span the $2\dim\Delta_n$-dimensional space. The conformal current of a linear field is the corresponding special conformal vector field of the flat model.

### The Two-Dimensional Exception

In dimension $n=2$ the normalisation $\frac1n$ and the weight of the twistor equation degenerate: the conformal group of a surface is infinite-dimensional, the twistor equation is a holomorphic condition on a line bundle rather than an overdetermined spinor system, and the space of solutions is infinite-dimensional, not $2\dim\Delta_2$. The article's statements are therefore stated for $n\ge3$, and the surface case is the concern of the two-dimensional conformal theory.

## Summary

The **Penrose operator** $\mathcal{P}_X\sigma=\nabla_X\sigma+\frac1nX\cdot D\sigma$ is the twistor operator of the conformal structure, written from the side of the equation; it is the composition $\pi\circ\nabla^{\mathcal{S}}$ of the covariant derivative with the projector onto the kernel of the Clifford contraction, its symbol is injective and it is overdetermined elliptic. Its kernel is the space of **twistor spinors**, and the twistor equation is **conformally invariant**: the zero set of $\mathcal{P}$ is an invariant of the conformal class $[g]$. Killing spinors are the twistor spinors with $D\sigma=-n\lambda\sigma$ for a constant $\lambda$; on the conformally flat model the twistor spinors form a $2\dim\Delta_n$-dimensional representation of the conformal algebra, on a complete Einstein manifold they are the sums of Killing spinors, and on a Ricci-flat manifold they are parallel. A twistor spinor produces a **conformal Killing field** through the current $X_{\sigma,\tau}=\sum_i(\sigma,e_i\cdot\tau)e_i$, which is the bridge to *Conformal Geometry*. The operator and its symbol are *The Twistor Operator*; the conformal quotient and the conformal model are *The Conformal Model of Euclidean Space*; the twistor space is *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{P}_X\sigma=\nabla_X\sigma+\tfrac1nX\cdot D\sigma$ | Penrose operator (= the twistor operator) |
| $\pi=\operatorname{id}-\frac1nc^*c$ | Projector onto $\ker c$; $\mathcal{P}=\pi\nabla^{\mathcal{S}}$ |
| $\mathcal{P}\sigma=0$ | Twistor equation; $\sigma$ a twistor spinor |
| $\nabla_X\sigma=\lambda X\cdot\sigma$ | Killing spinor with constant $\lambda$ |
| $D\sigma=-n\lambda\sigma$ | Relation between the two equations |
| $\hat g=\Omega^2g$, $\hat\sigma$ | Conformal change and the weighted identification |
| $X_\sigma=\sum_i(\sigma,e_i\cdot\sigma)e_i$ | Conformal current of a twistor spinor |
| $\mathcal{L}_{X_\sigma}g=\tfrac2n(\operatorname{div}X_\sigma)g$ | Conformal Killing equation |
| $2\dim\Delta_n$ | Dimension of the flat twistor-spinor space, $n\ge3$ |

## Further Reading

- Helga Baum, Thomas Friedrich, Ralf Grunewald and Ines Kath, *Twistors and Killing Spinors on Riemannian Manifolds* (Teubner, 1991), for the Penrose operator, the twistor equation and its conformal invariance.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time, Volume 2* (Cambridge University Press, 1986), for the conformal Killing spinors and the twistor programme.
- Thomas Friedrich, *Dirac Operators in Riemannian Geometry* (American Mathematical Society, 2000), for the twistor and Killing spinor equations, the conformal weights and the conformal covariance.
- Helga Baum, "Conformal Killing Spinors and Special Geometric Structures in Lorentzian Geometry", *Proceedings of the International Congress of Mathematicians* (2002), for the conformal version of the equation and the construction of the conformal current.
- Michael Eastwood and Jan Slovák, "Conformal Geometry and Globally Conformally Flat Manifolds", in *The Penrose Transform and Analytic Cohomology in Representation Theory* (American Mathematical Society, 1993), for the parabolic-geometry view of the same operator.
