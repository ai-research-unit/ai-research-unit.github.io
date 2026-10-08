
# __Hermitian Pairings and the Index__

## Introduction

A **Hermitian pairing** on a module is a sesquilinear form with a conjugate symmetry, positive definite when the module is a Hilbert module; it is the structure with which the index of an operator is read. On the analytic side the kernel and cokernel of an elliptic operator carry Hermitian forms, and the **index** is a pairing between them: the difference of the dimensions is the pairing of the two Hermitian spaces, and for a self-adjoint operator it is the **signature** of the Hermitian form on the kernel. On the topological side the index is a pairing of $K$-theory and $K$-homology, $\langle[\sigma_D],[M]\rangle$, computed through the Chern character and the characteristic classes, and the Hermitian structure is what makes the pairing valued in the real numbers and the integrality of the index a statement about the Hermitian forms involved. The article draws together the Hermitian pairings of the corpus, the index pairing of $K$-theory, and the Hermitian structure of the index.

The article develops the Hermitian pairing and its positivity, the **index pairing** of an elliptic operator as the pairing of its symbol class with the fundamental class, the Hermitian structure of the kernel and cokernel and the identification of the index with a signature, the Chern-character form of the pairing, and the real and mod-two refinements. The Hermitian pairings on a topological space and on an involution ring are those of the Part II articles *Hermitian Pairings on a Topological Space*, *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint* and *Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint*; the Atiyah–Singer theorem and the index pairing are those of *The Atiyah–Singer Index Theorem and K-Theory*; the signature and its adjoint are *The Signature Operator* and *The Adjoint of the Signature Operator*; the spin index and its adjoint are *The Dirac Operator on a Manifold* and *The Dirac Operator and Its Adjoint*; and the Hermitian index theorem and the $\chi_y$-genus are *The Hermitian Index Theorem and the Signature Operator*.

The prerequisites are *Hermitian Pairings on a Topological Space* for the Hermitian and bilinear pairings, the orthogonal decomposition and the signature of the fixed part; the Part I articles *Bilinear Forms* and *Indefinite Inner Product Spaces* for the forms and the signature; *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint* and *Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint* for the Hermitian forms over an involution and an algebra; *The Atiyah–Singer Index Theorem and K-Theory* for the index theorem, the symbol class and the pairing; *K-Theory* and *Characteristic Classes* for the $K$-theory and the Chern character; and *The Adjoint of the Signature Operator* and *The Dirac Operator and Its Adjoint* for the analytic self-adjointness and the kernel pairings. The Hermitian structure is the chosen form, and the whole article is the geometry of that choice. No physics is invoked.

## Hermitian Pairings

**Definition.** Let $A$ be a ring with an involution $*$, and let $M$ be a right $A$-module. A **Hermitian pairing** on $M$ is a biadditive map $\phi:M\times M\to A$ that is $A$-linear in the second variable and conjugate-linear in the first,

$$
\phi(xa,y)=\phi(x,y)a,\qquad
\phi(x,ya)=\phi(x,y)a,\qquad
\phi(y,x)=\phi(x,y)^{*} ,
$$

with the last the **Hermitian symmetry**; the form is **positive definite** when $\phi(x,x)$ is a positive element of $A$ for $x\neq0$, and the pair $(M,\phi)$ is a **Hermitian module**. The **signature** of a Hermitian pairing on a finite-dimensional real or complex space is the difference of the numbers of positive and negative eigenvalues, $\sigma=p-q$; the **Witt group** classifies the forms up to the addition of hyperbolic planes, and the classification of the Hermitian forms over an involution ring is that of *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.

**Theorem (the pairing of a topological space).** Let $X$ be a compact space with a continuous involution $\iota$, and let $\phi$ be a Hermitian pairing on the cohomology $H^{*}(X;\mathbb{C})$ that is compatible with the involution. Then the cohomology decomposes orthogonally into the eigenspaces of $\iota$, the pairing restricted to each eigenspace is nondegenerate, and the signatures of the restrictions determine the pairing up to isometry:

$$
H^{*}(X;\mathbb{C})=H^{+}\oplus H^{-},\qquad
\phi=\phi_{+}\perp\phi_{-},\qquad
\operatorname{sign}\phi=\operatorname{sign}\phi_{+}+\operatorname{sign}\phi_{-} .
$$

**Proof.** The compatibility of the pairing with the involution and its Hermitian symmetry make the eigenspaces orthogonal and the restrictions nondegenerate; the orthogonal decomposition and the additivity of the signature are the elementary linear algebra of an isometric involution on a Hermitian space. The statement is that of *Hermitian Pairings on a Topological Space*. $\square$

**Remark.** The signature of the fixed part is the invariant that the index refines: for the signature operator the index is the signature of the intersection form on the harmonic middle forms, and for the Dirac operator it is the difference of the dimensions of the chiral zero modes, which is the trace of the chirality on the kernel. Both are Hermitian pairings with an involution, and the index is the integer attached to them.

## The Index Pairing

**Definition.** Let $M$ be a closed smooth manifold and let $D$ be an elliptic operator on the sections of a complex vector bundle over $M$. Its **symbol class** is the compactly supported class

$$
[\sigma_D]\in K^{0}(T^{*}M),\qquad
\sigma_D(x,\xi)=D_{1}(x,\xi)
$$

of the principal symbol, an element of the $K$-theory of the cotangent bundle with compact supports; the **fundamental class** of the tangent bundle is

$$
[M]\in K_{0}(T^{*}M),
$$

the $K$-homology class of the Dirac-type operator along the fibres; and the **index pairing** is the evaluation

$$
\operatorname{ind}D=\bigl\langle[\sigma_D],[M]\bigr\rangle ,
$$

the integer obtained by pairing the symbol class with the fundamental class.

**Theorem (the index theorem as a pairing).** The analytic index of $D$ is the pairing of its symbol class with the fundamental class,

$$
\operatorname{ind}D=\bigl\langle[\sigma_D],[M]\bigr\rangle ,
$$

and the pairing is computed through the Chern character by

$$
\bigl\langle[\sigma_D],[M]\bigr\rangle
=\int_{T^{*}M}\operatorname{ch}([\sigma_D])\wedge\operatorname{td}(TM\otimes\mathbb{C})\Big|_{\text{Todd class}},
$$

the **Atiyah–Singer index theorem**; for the operators of this category the general pairing specialises to the signature $\int_ML(TM)$, the $\hat A$-genus $\int_M\hat A(TM)$ and the holomorphic Euler characteristic $\int_M\operatorname{ch}(E)\operatorname{td}(TM)$.

**Proof sketch.** The topological index is defined by the pushforward in $K$-theory along the embedding of $M$ in a Euclidean space, and the theorem identifies it with the analytic index by the heat-kernel argument; the Chern-character formula is the evaluation of the pushforward by the Riemann–Roch theorem for the embedding. The theorem, the symbol class and the pairing are those of *The Atiyah–Singer Index Theorem and K-Theory*; the specialisations are those of *The Signature Operator*, *The Dirac Operator on a Manifold* and *The Hermitian Index Theorem and the Signature Operator*. $\square$

**Remark.** The pairing is the topological expression of the index, and it is **Hermitian** in the sense that the Chern character is the pairing of the $K$-theory with the cohomology, valued in the real numbers through the fundamental class; the integrality of the index is the statement that the pairing takes integer values when the symbol comes from a genuine elliptic operator, which is the Atiyah–Singer integrality theorem.

## The Hermitian Structure of the Index

**Theorem (the pairings of the kernel and cokernel).** Let $D:\Gamma(E)\to\Gamma(F)$ be an elliptic operator between Hermitian bundles over a closed manifold, with formal adjoint $D^{*}$. Then on the finite-dimensional spaces $\ker D$ and $\operatorname{coker}D\cong\ker D^{*}$ there are Hermitian forms, and the index is the difference of their dimensions,

$$
\operatorname{ind}D=\dim\ker D-\dim\ker D^{*},
$$

so the index is the **Hermitian pairing** of the two kernel spaces: the difference of the dimensions is the pairing of the Hermitian forms, and the analytic index is valued in $\mathbb{Z}$ because the forms are the positive forms of the $L^{2}$ inner products restricted to the kernels.

**Proof.** The Hermitian metrics on $E$ and $F$ give the $L^{2}$ inner products, and the restriction to the finite-dimensional kernels is positive definite by definition; the cokernel of $D$ is the kernel of $D^{*}$ by the Fredholm alternative, and the index is the difference of the dimensions. The positivity is what makes the index a difference of two positive quantities and hence an integer. $\square$

**Theorem (the index as a signature).** Let $D$ be a self-adjoint elliptic operator graded by an involution $\tau$ with $\tau D\tau^{-1}=-D$, so that $D$ is odd and splits into the mutually adjoint halves $D^{\pm}$. Then the index of the half is the **signature** of the Hermitian form on the kernel,

$$
\operatorname{ind}D^{+}=\operatorname{tr}(\tau\mid\ker D)=\sigma(\ker D,\tau),
$$

the difference of the dimensions of the two eigenspaces of $\tau$ on the kernel; for the signature operator this is the signature of the middle intersection form, and for the Dirac operator the difference of the dimensions of the chiral zero-mode spaces.

**Proof.** The kernel of the self-adjoint operator splits into the two eigenspaces of the involution $\tau$, which are the kernels of the two halves because $\tau D=-D\tau$; the trace of $\tau$ on the kernel is the difference of the two dimensions, and it is the signature of the Hermitian form whose positive and negative parts are the two eigenspaces. The statements for the signature and the Dirac operators are those of *The Adjoint of the Signature Operator* and *The Dirac Operator and Its Adjoint*. $\square$

**Corollary (the Hermitian structure of the index).** The index of a self-adjoint graded operator is the invariant of the pair (Hermitian form, involution) on the kernel, and it is the **Hermitian structure** that makes the index an integer of definite sign: the $L^{2}$ form is positive definite, the involution splits it into a positive and a negative part, and the index is the signature of the split. This is the analytic form of the Hermitian pairing of *Hermitian Pairings on a Topological Space*, with the cohomology replaced by the kernel and the involution by the chirality.

## The Pairing with the Chern Character

**Theorem (the Chern-character pairing).** The index pairing is computed by the Chern character,

$$
\operatorname{ind}D=\int_{M}\operatorname{ch}(E)\,\rho(TM),
$$

where $E$ is the bundle of the operator and $\rho(TM)$ is the characteristic class of the symbol — the Todd class for the Dolbeault operator, the $\hat A$-class for the spin operator, the $L$-class for the signature operator; the pairing of the $K$-theory class of $E$ with the cohomology class $\rho$ is the **Hermitian pairing** of the two, and the multiplicativity of the Chern character, $\operatorname{ch}(E\oplus F)=\operatorname{ch}(E)+\operatorname{ch}(F)$ and $\operatorname{ch}(E\otimes F)=\operatorname{ch}(E)\operatorname{ch}(F)$, is what makes the index additive and multiplicative in the natural sense.

**Proof.** The Chern character of the symbol class of the operator is $\operatorname{ch}(E)\rho(TM)$ by the multiplicativity and the definition of $\rho$ as the Chern character of the symbol of the relevant Dirac-type operator; the pairing is the evaluation on the fundamental class, and the additivity and multiplicativity are those of the index and of the Chern character of *The Hermitian Index Theorem and the Signature Operator*. $\square$

**Remark.** The three characteristic classes of the category are the three values of one construction: the Todd class gives the holomorphic index, the $\hat A$-class the spin index and the $L$-class the signature, and the three are the pairings of the corresponding $K$-theory classes with the fundamental class. The Chern-character pairing is the topological side of the Hermitian pairing of the kernel.

## The Real and Mod-Two Index

**Definition.** A **real structure** on the operator is an antilinear involution commuting with $D$ and with the chirality; the kernel then carries a real structure, and the **mod-two index** is the dimension of the real kernel modulo two,

$$
\operatorname{ind}_2 D=\dim_{\mathbb{R}}\ker D\pmod 2 ,
$$

an invariant of the real operator and a refinement of the integer index.

**Theorem.** The mod-two index is well defined for a real self-adjoint graded operator and is computed by the Stiefel–Whitney classes; for the Dirac operator of a spin four-manifold the mod-two index is the Kervaire–Milnor invariant, and the vanishing of the mod-two index of the spin operator is equivalent to Rökhlin's theorem that the signature of a closed spin four-manifold is divisible by $16$.

**Proof sketch.** The real structure makes the complex kernel into the complexification of a real vector space, and the dimension modulo two is the dimension of that real space, invariant under the deformations of the operator because the real index is locally constant; the computation by the Stiefel–Whitney classes is the real index theorem in the $\mathbb{Z}/2$ setting, and the identification with Rökhlin's theorem is the mod-two refinement of the $\hat A$-index. The real index theory is in *The Atiyah–Singer Index Theorem and K-Theory* and *Spin Geometry*. $\square$

**Remark.** The Hermitian structure of the index has three refinements: the integer index of the complex pairing, the signature of the self-adjoint graded operator, and the mod-two index of the real operator. Each is a pairing of the kernel with the appropriate form — complex Hermitian, Hermitian with an involution, real symmetric — and the trichotomy of real, complex and quaternionic structures is the one of *Spinor Adjoints and the Dirac Adjoint with Hermitian Adjoint* and *Real Spinors and Reality Conditions with Inner Conjugation*.

## Examples

**Example (the Dolbeault pairing).** For the Dolbeault operator of a Hermitian holomorphic bundle $E$ over a compact complex manifold the index pairing is the holomorphic Euler characteristic, $\operatorname{ind}=\int_M\operatorname{ch}(E)\operatorname{td}(TM)$, and the Hermitian structure is that of the Bergman-type positivity of the harmonic $(0,q)$-forms with coefficients in $E$; the kernel and cokernel are the harmonic forms of the two parities, and the index is the difference of their dimensions. This is the pairing of *The Hermitian Index Theorem and the Signature Operator*.

**Example (the signature pairing).** For the signature operator of a closed oriented $4k$-manifold the index pairing is the signature, $\operatorname{ind}D^{+}=\int_ML(TM)$, and the Hermitian structure is the intersection form on the middle harmonic forms; the positive and negative definite parts are the self-dual and anti-self-dual forms, and the index is the difference of their dimensions. This is the pairing of *The Signature Operator* and *The Adjoint of the Signature Operator*.

**Example (the spin pairing).** For the Dirac operator of a closed spin manifold the index pairing is the $\hat A$-genus, $\operatorname{ind}D^{+}=\int_M\hat A(TM)$, and the Hermitian structure is the spinor inner product restricted to the chiral zero modes; the positive scalar curvature vanishing theorem is the statement that the Hermitian form of the kernel is zero. The twisted version pairs the Chern character of the twisting bundle, and the mod-two refinement gives Rökhlin's theorem. This is the pairing of *The Dirac Operator on a Manifold* and *The Dirac Operator and Its Adjoint*.

**Example (the finite-dimensional model).** For a self-adjoint endomorphism of a finite-dimensional Hermitian space graded by an involution, the index of the positive part is the signature of the form restricted to the kernel, and the Chern-character pairing reduces to the identity pairing of a finite-dimensional $K$-theory class with itself; the model is the one-dimensional shadow of every construction above, and it is the finite-dimensional case of *Hermitian Pairings on a Topological Space*.

## Summary

A **Hermitian pairing** is a sesquilinear form with conjugate symmetry, positive definite on a Hermitian module, with **signature** $p-q$ and a Witt-group classification; the pairing of a space with an involution decomposes orthogonally into the eigenspaces and the signature is additive over them. The **index pairing** of an elliptic operator is the evaluation of its symbol class against the fundamental class, $\operatorname{ind}D=\langle[\sigma_D],[M]\rangle$, computed by the Atiyah–Singer theorem through the **Chern character**, $\operatorname{ind}D=\int_M\operatorname{ch}(E)\rho(TM)$, with the Todd, $\hat A$ and $L$ classes giving the holomorphic, spin and signature indices. The **Hermitian structure of the index** is the analytic form of the pairing: the kernel and cokernel carry the $L^{2}$ Hermitian forms, the index is their difference, and for a self-adjoint operator graded by an involution the index is the **signature of the Hermitian form on the kernel**, $\operatorname{ind}D^{+}=\operatorname{tr}(\tau\mid\ker D)$ — the signature of the middle intersection form for the signature operator and the difference of the chiral zero-mode dimensions for the Dirac operator. The **mod-two index** of a real operator is the real refinement, computed by the Stiefel–Whitney classes and giving Rökhlin's divisibility $16\mid\sigma$ in dimension four. The integer, the signature and the mod-two invariants are the three refinements of one Hermitian pairing, and the whole category of this Part is their geometry.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\phi$, $\phi(y,x)=\phi(x,y)^{*}$ | Hermitian pairing on a module with an involution |
| $\sigma=p-q$, Witt group | Signature and classification of a Hermitian form |
| $H^{*}=H^{+}\oplus H^{-}$, $\phi=\phi_{+}\perp\phi_{-}$ | Orthogonal decomposition under an involution |
| $[\sigma_D]\in K^{0}(T^{*}M)$, $[M]\in K_{0}(T^{*}M)$ | Symbol class and fundamental class |
| $\operatorname{ind}D=\langle[\sigma_D],[M]\rangle$ | Index pairing |
| $\operatorname{ind}D=\int_M\operatorname{ch}(E)\rho(TM)$ | Chern-character form of the pairing |
| $\rho=$ Todd, $\hat A$, $L$ | Holomorphic, spin and signature indices |
| $\operatorname{ind}D=\dim\ker D-\dim\ker D^{*}$ | Index as the pairing of the kernels |
| $\operatorname{ind}D^{+}=\operatorname{tr}(\tau\mid\ker D)=\sigma(\ker D,\tau)$ | Index as the signature of the kernel pairing |
| $\operatorname{ind}_2D=\dim_{\mathbb{R}}\ker D\pmod2$ | Mod-two index; Rökhlin $16\mid\sigma$ in dimension four |

## Further Reading

- Michael F. Atiyah and Isadore M. Singer, "The index of elliptic operators I, III," *Annals of Mathematics* **87** (1968), 484–530 and 546–604, for the index pairing, the symbol class and the topological index.
- Michael F. Atiyah, *K-Theory* (Benjamin, 1967), for the $K$-theory, the Chern character and the index pairing.
- Friedrich Hirzebruch, *Topological Methods in Algebraic Geometry*, Classics in Mathematics (Springer, 1995), for the Chern character, the characteristic classes and the Riemann–Roch theorem.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the spin index, the mod-two index and Rökhlin's theorem.
- Max Karoubi, *K-Theory: An Introduction* (Springer, 1978), for the $K$-theory with involution, the Hermitian forms and the index pairing.
- Phillip A. Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Hermitian pairings, the positivity and the Hodge index theorem.
- C. T. C. Wall, *Surgery on Compact Manifolds* (Academic Press, 1970), for the Hermitian forms and the Witt group in the topological setting.
