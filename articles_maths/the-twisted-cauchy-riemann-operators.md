
# __The Twisted Cauchy–Riemann Operators__

## Introduction

The Cauchy–Riemann operator of a spin manifold acts on the spinor bundle, $D=c\circ\nabla^{\mathcal{S}}:\Gamma(\mathcal{S})\to\Gamma(\mathcal{S})$, and it has a **twisted** version: for a Clifford module $W$ over the same manifold, with a connection whose parallel transport is compatible with the Clifford action, the operator

$$
D_W = \sum_i c(e_i)\,\nabla^{\mathcal{S}\otimes W}_{e_i} : \Gamma(\mathcal{S}\otimes W)\longrightarrow\Gamma(\mathcal{S}\otimes W)
$$

acts on the twisted spinor bundle, and it is again a first-order, formally self-adjoint, elliptic operator of odd parity. The **twisted Cauchy–Riemann operators** are the operators of this form; they are the natural analytic objects of the twistor programme, where the twisting module is a power of the spinor bundle or a bundle of forms, and where the twisted equation $D_W\phi=0$ is the massless field equation in disguise.

The article treats three things: the definition and the first properties of the twisted operator, the **Lichnerowicz formula** with the twist, in which the curvature of the twisting module appears as a zeroth-order term, and the concrete operators of the twistor transform, which are the twisted Cauchy–Riemann operators at the level of the positive and negative spinor bundles. The index of the twisted operator is the topological statement of *Clifford Modules and the Twisted Cauchy–Riemann Operator*, and the analytic theory — the spectrum, the heat kernel, the closed extensions — is *Dirac Differential Operators* in Part III; neither is repeated here.

**The boundaries.** The untwisted operator, the spin connection and the Lichnerowicz formula are *The Spinor Operator*; the adjoint theory is *The Adjoint of the Clifford Multiplication* and *The Codifferential on a Spinor Bundle*; the twistor operator and the twistor equation are *The Twistor Operator* and *The Penrose Operator*; the twistor correspondence and the transform are *Hermitian Spin Geometry and the Twistor Correspondence*; the index is *Clifford Modules and the Twisted Cauchy–Riemann Operator* and the analysis is *Dirac Differential Operators*. The body is a Riemannian spin manifold with $c(v)^2=-g(v,v)\operatorname{id}$, $c(v)^*=-c(v)$, a Clifford module $W$ and a connection on $W$ compatible with the Clifford action.

## The Twisted Operator

**Definition.** Let $W$ be a Clifford module over $M$ with a connection $\nabla^W$ satisfying $\nabla^W(c(a)w)=c(\nabla^{\mathrm{LC}}a)w+c(a)\nabla^Ww$ for sections $a$ of the Clifford bundle; the **twisted Cauchy–Riemann operator** is the composition of the twisted covariant derivative with the Clifford contraction,

$$
D_W = c\circ\nabla^{\mathcal{S}\otimes W} , \qquad D_W(\sigma\otimes w)=\sum_i (e_i\cdot\sigma)\otimes\nabla^W_{e_i}w + \sum_i (e_i\cdot\nabla^{\mathcal{S}}_{e_i}\sigma)\otimes w .
$$

**Proposition.** The operator $D_W$ is of first order, it is an **odd** operator for the chirality grading when the grading of $W$ is taken into account, its principal symbol is the Clifford multiplication $\xi\mapsto c(\xi^{\sharp})$ tensored with the identity of $W$, so it is elliptic with invertible symbol; it is formally self-adjoint for the tensor product of the fibre forms when the connection $\nabla^W$ is compatible with the form on $W$, and it is the untwisted operator when $W$ is the trivial module with the trivial connection.

**Proof.** The first-order and symbol statements are read from the definition, the symbol being the Clifford multiplication on each factor, invertible for $\xi\ne0$ because $c(\xi)^2=-g(\xi,\xi)\operatorname{id}$; the parity is the parity of the Clifford multiplication tensored with the parity of the module, and the formal self-adjointness is the untwisted computation of *The Spinor Operator* with the inner product extended to the twist and the compatibility of $\nabla^W$ used for the integration by parts. The trivial case is immediate.

**Remark (why "twisted Cauchy–Riemann").** The corpus names $D$ the Cauchy–Riemann operator and the operators of this article the twisted Cauchy–Riemann operators; the classical name of $D_W$ is the twisted Dirac operator, and it is glossed here once for the reader arriving from the physics or index-theory literature. The name used throughout is the twisted Cauchy–Riemann operator.

## The Lichnerowicz Formula with Twist

**Theorem (the twisted Lichnerowicz formula, quoted).** For a Clifford-compatible connection on $W$,

$$
D_W^2 = \nabla^{*}\nabla + \tfrac14\operatorname{scal} + \mathcal{R}^W ,
$$

where $\nabla^{*}\nabla$ is the connection Laplacian of $\mathcal{S}\otimes W$, $\operatorname{scal}$ is the scalar curvature of $g$, and $\mathcal{R}^W$ is the zeroth-order term obtained by the Clifford contraction of the curvature $R^W$ of the twisting connection,

$$
\mathcal{R}^W(\sigma\otimes w) = \tfrac12\sum_{i<j} c(e_i)c(e_j)\,\sigma\otimes R^W(e_i,e_j)w .
$$

**Proof sketch.** The square of the operator is computed by the Weitzenböck method: the second-order terms give the connection Laplacian with a sign, and the zeroth-order remainder is the Clifford contraction of the total curvature, which splits into the spinor curvature (giving the scalar curvature term) and the twist curvature (giving $\mathcal{R}^W$). The untwisted case is *The Spinor Operator*, and the twist term is the standard addition quoted from *Clifford Modules and the Twisted Cauchy–Riemann Operator* and the heat-kernel literature.

**Corollary (vanishing theorems).** If the zeroth-order term $\frac14\operatorname{scal}+\mathcal{R}^W$ is a positive operator on the relevant subspace, then $D_W$ has no harmonic sections of the corresponding chirality, by integration of $D_W^2$; the corollary is the twisted form of the Bochner method and is the standard application of the formula.

**Proof.** For a harmonic section $\phi$ with $D_W\phi=0$, integration of the formula gives $\int\lvert\nabla\phi\rvert^2+\int\langle(\frac14\operatorname{scal}+\mathcal{R}^W)\phi,\phi\rangle=0$; if the zeroth-order operator is positive definite on $\phi$, the equality forces $\phi=0$. The argument is the untwisted one with the twist term included.

**Remark (the twist curvature and the geometry).** The term $\mathcal{R}^W$ is the reason the twisted operator is not the untwisted one on a larger bundle: the curvature of the twist acts by Clifford multiplication and can contribute a definite sign, and the vanishing theorems of the category are read from the total zeroth-order operator. The formula is the analytic bridge between the curvature of the manifold, the curvature of the twist, and the kernel of the operator.

## The Twisted Operators of the Twistor Transform

**Proposition (the spinor-bundle twist).** For $W=\mathcal{S}$ there is the standard identification of Clifford modules $\mathcal{S}\otimes\mathcal{S}\cong\Lambda^\bullet T^*M$ (up to the chirality bookkeeping), and the twisted Cauchy–Riemann operator becomes the operator $d+d^*$ of the de Rham complex on the exterior bundle; for this twist the Lichnerowicz formula is the Weitzenböck formula of the de Rham Laplacian.

**Proof.** The identification is the standard Clifford-module isomorphism: the endomorphisms of the spin module are the Clifford algebra, and the Clifford algebra of the tangent space is the exterior algebra as a vector space, with the Clifford multiplication corresponding to $v^\flat\wedge-\iota_v$; under this correspondence $D_{\mathcal{S}}$ acts as $d+d^*$, which is the statement of *Spin Geometry* and *Clifford Modules and the Twisted Cauchy–Riemann Operator*. The Weitzenböck formula is the specialisation of the twisted Lichnerowicz formula.

**Proposition (the operators of the transform).** On a four-dimensional manifold the twistor transform is built from the twisted Cauchy–Riemann operators between the twisted spinor bundles; the operator

$$
\mathcal{D} : \Gamma(\mathcal{S}^-\otimes W)\longrightarrow\Gamma(T^*M\otimes\mathcal{S}^-\otimes W)
$$

with the projection onto the trace-free part is the twisted operator of the correspondence, its kernel consists of the twistor-like fields of the twist, and the massless field equations of the twistor programme are its twisted equations.

**Proof sketch.** The correspondence of *Hermitian Spin Geometry and the Twistor Correspondence* associates to the field on $M$ the restriction of a holomorphic object on $Z(M)$; the differential operator whose kernel is the space of these fields is the twisted Cauchy–Riemann operator of the appropriate twist, and the projection to the trace-free part is the twistor projection of *The Twistor Operator*. The analytic derivation is the Penrose-transform literature, quoted; the structural statement is what the article retains.

**Remark.** The twisted operators of the transform are the reason the twistor programme is an analytic theory: the holomorphic data on $Z(M)$ are the solutions of the twisted Cauchy–Riemann equations on $M$, and the transform is the correspondence between the two descriptions. The operator of *The Twistor Operator* is the untwisted member of the family, the one that defines the twistor spinors.

## Worked Cases

### The Flat Torus

On the flat torus with a twisting line bundle of curvature zero the twisted operator is the untwisted one on each Fourier mode, and the twist contributes only through the holonomy of $\nabla^W$; the Lichnerowicz formula reduces to $D_W^2=-\Delta$ on the twisted bundle.

### The Spinor-Bundle Twist

For $W=\mathcal{S}$ the twisted operator is $d+d^*$ on the forms, the twist curvature term is the Riemann curvature contribution, and the formula becomes the classical Weitzenböck formula of the Hodge Laplacian; this is the model case in which the twist is the geometry itself.

### A Curved Twist

For a twist whose curvature is a nonzero multiple of the Clifford volume element, the twist term $\mathcal{R}^W$ is a constant, and the twisted operator satisfies $D_W^2=\nabla^*\nabla+\text{constant}$; the vanishing theorems are read from the sign of the constant, and the example shows the twist term entering as a shift of the scalar curvature.

## Summary

The **twisted Cauchy–Riemann operators** are $D_W=\sum_ic(e_i)\nabla^{\mathcal{S}\otimes W}_{e_i}$ on the twisted spinor bundle of a Clifford module $W$ with a Clifford-compatible connection; they are first-order, elliptic with invertible symbol, formally self-adjoint, odd for the chirality, and reduce to $D$ for the trivial twist. The **twisted Lichnerowicz formula** is $D_W^2=\nabla^*\nabla+\frac14\operatorname{scal}+\mathcal{R}^W$, with the twist curvature $\mathcal{R}^W$ given by the Clifford contraction of $R^W$, and it is the source of the vanishing theorems of the category. The twist by the spinor bundle gives the identification $\mathcal{S}\otimes\mathcal{S}\cong\Lambda^\bullet T^*M$ and the operator $d+d^*$ on forms, and the twisted operators between the chiral twisted spinor bundles are the operators of the twistor transform, whose kernels are the massless fields of *Hermitian Spin Geometry and the Twistor Correspondence*. The index of the twisted operator is *Clifford Modules and the Twisted Cauchy–Riemann Operator*, the analysis is *Dirac Differential Operators*, and the untwisted case is *The Spinor Operator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\nabla^{\mathcal{S}\otimes W}$ | Twisted spin connection |
| $D_W=\sum_ic(e_i)\nabla^{\mathcal{S}\otimes W}_{e_i}$ | Twisted Cauchy–Riemann operator |
| $c(\xi)$ symbol | Elliptic, invertible for $\xi\ne0$ |
| $D_W^*=D_W$ | Formal self-adjointness |
| $D_W^2=\nabla^*\nabla+\frac14\operatorname{scal}+\mathcal{R}^W$ | Twisted Lichnerowicz formula |
| $\mathcal{R}^W=\frac12\sum_{i<j}c(e_i)c(e_j)\otimes R^W(e_i,e_j)$ | Twist curvature term |
| $\mathcal{S}\otimes\mathcal{S}\cong\Lambda^\bullet T^*M$, $D_{\mathcal{S}}=d+d^*$ | Spinor-bundle twist |
| $\mathcal{D}$ on $\Gamma(\mathcal{S}^-\otimes W)$ | Twisted operator of the twistor transform |

## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the twisted Dirac operator, the Lichnerowicz formula with twist and the spinor-bundle identification.
- Nicole Berline, Ezra Getzler and Michèle Vergne, *Heat Kernels and Dirac Operators* (Springer, 1992), for the twisted operators, their symbols and the Weitzenböck formulas.
- Thomas Friedrich, *Dirac Operators in Riemannian Geometry* (American Mathematical Society, 2000), for the twisted Cauchy–Riemann operators and the vanishing theorems.
- R. S. Ward and Raymond O. Wells, *Twistor Geometry and Field Theory* (Cambridge University Press, 1990), for the twisted operators of the twistor transform and the massless field equations.
- Michael F. Atiyah, Nigel J. Hitchin and Isidore M. Singer, "Self-Duality in Four-Dimensional Riemannian Geometry", *Proceedings of the Royal Society of London A* 362 (1978), 425–461, for the twistor correspondence and its analytic operators.
