
# __Dirac Operators with Hermitian Adjoint__

## Introduction

A Dirac operator on a Hermitian Clifford module is the composition of the two structures the corpus has built so far: the one-sided Clifford action of *The Adjoint of the One-Sided Action with Hermitian Adjoint*, which is skew-adjoint for the vectors, and a first-order operator whose formal adjoint is minus itself. The product of two skew-adjoint factors is self-adjoint, and this article is about the operator so produced — the **Dirac operator as a Hermitian operator**: its self-adjointness with respect to the module form, the positivity of its Hermitian square, the reality of its spectrum, the orthogonality of its eigenspinors, the splitting of the module by its kernel, and the finite-dimensional model in which every statement is an explicit computation.

The boundary is sharp. The analytic theory of these operators — formal and essential self-adjointness, domains, closures, the spectrum of the flat model, the compact resolvent and the index of the chiral part — is *Dirac Differential Operators*, and this article cites it and does not repeat it. The vector derivative and the Cauchy–Riemann operator are *Geometric Calculus and the Vector Derivative* and *Clifford Analysis*; the monogenic functions are named there; the geometric constructions are Part IV. What is established here is the **Hermitian structure** of the operator: that the module form makes it self-adjoint, that its square is a positive operator, and that the finite-dimensional case is a Hermitian endomorphism of a Hermitian space, with the spectral consequences that follow from that alone.

The Clifford action and the adjoint are *The Adjoint of the One-Sided Action with Hermitian Adjoint*; the module form and the Hermitian Clifford module are *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*; the blade form and the positivity of the square are *The Blade Form and the Hermitian Structure with Hermitian Adjoint* and *Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint*; the self-adjoint operators and their spectra are *Self-Adjoint and Skew Operators with Hermitian Adjoint* and *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*; the spinor module, its chirality and the index are *Spinors as Minimal Left Ideals with Inner Conjugation*, *Spin Representations and Clifford Modules with Inner Conjugation* and *Dirac Differential Operators*; and the analytic statements are *Dirac Differential Operators* and *Unbounded Operators and Spectral Measures*.

## The Dirac Operator and the Hermitian Form

### Definition

**Definition.** Let $S$ be a Hermitian Clifford module over $\mathrm{Cl}(V,q)$ with form $(\cdot,\cdot)$, let $e_1,\dots,e_m$ be an orthonormal frame of $V$, and let $\partial_1,\dots,\partial_m$ be first-order operators on $S$ with formal adjoints $\partial_j^{*} = -\partial_j$. The **Dirac operator** is

$$
D = \sum_{j=1}^{m} \rho(e_j)\,\partial_j ,
$$

where $\rho$ is the one-sided Clifford action. The operator $D^2$ is the **Hermitian square**.

**Remark (the two skew factors).** The operator is written as a sum of products of two factors, and each factor is skew-adjoint: the Clifford coefficient because $\rho(e_j)^{*} = \rho(e_j^{\dagger}) = -\rho(e_j)$ for a vector, and the first-order operator by hypothesis. This is the structural description of a Dirac operator, and every property below is a consequence of it.

### Self-Adjointness

**Theorem.** The Dirac operator is formally self-adjoint:

$$
D^{*} = D .
$$

**Proof.** By the composite rule of *The Adjoint of the One-Sided Action with Hermitian Adjoint*, $(\rho(e_j)\partial_j)^{*} = \partial_j^{*}\rho(e_j^{\dagger}) = (-\partial_j)(-\rho(e_j)) = \rho(e_j)\partial_j$, the two sign flips cancelling; summing gives $D^{*} = D$.

**Corollary (the reality and the orthogonality of the spectrum).** A formally self-adjoint operator has real spectrum; on a finite-dimensional Hermitian space, and in the spectral problem of a self-adjoint operator in general, the eigenspaces are mutually orthogonal and the eigenvectors form an orthonormal basis. These are the standard consequences of self-adjointness with respect to a Hermitian form, and the spectral theory is *Unbounded Operators and Spectral Measures*; the finite-dimensional case is *Self-Adjoint and Skew Operators with Hermitian Adjoint* and *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*.

### The Hermitian Square and Positivity

**Theorem.** For every $s$ in the module $S$ (in the analytic setting, for every $s$ in the domain of $D$),

$$
(D^2 s, s) = (Ds, Ds) = \lVert Ds\rVert^{2} \ge 0 ,
$$

so $D^2$ is a **positive** operator; and $D^{2} = D^{*}D$ because $D$ is self-adjoint. In particular $D$ has no negative eigenvalue and its kernel is the set of $s$ with $\lVert Ds\rVert = 0$.

**Proof.** $(D^2s,s) = (D(Ds),s) = (Ds, D^{*}s) = (Ds,Ds)$, using the self-adjointness of $D$; the norm expression is the positivity of the form of *Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint*, and the kernel statement follows because $\lVert Ds\rVert = 0$ iff $Ds = 0$ for a positive definite form.

**Corollary (the kernel is the harmonic spinors).** The kernel of $D$ consists of the **harmonic spinors**, the solutions of $Ds = 0$. On a closed manifold they form a finite-dimensional space with a positive definite Hermitian form, and on the flat model the kernel is trivial; both statements belong to the analysis of *Dirac Differential Operators*, and what the Hermitian structure adds is that the form on the kernel is the restriction of a positive definite form on the whole module, so the kernel is a Hermitian subspace in its own right.

### The Splitting of the Module by the Kernel

**Theorem (Hodge splitting).** Let $S$ be finite-dimensional (or, in the analytic setting of *Dirac Differential Operators*, let $D$ have closed range with finite-dimensional kernel). Then $S$ decomposes orthogonally,

$$
S = \ker D \oplus D(S) = \ker D \oplus \operatorname{im} D ,
$$

and the two summands are orthogonal and $D$-invariant.

**Proof.** For a self-adjoint operator on a Hermitian space, $\overline{\operatorname{im}D} = (\ker D)^{\perp}$, because $s \perp \operatorname{im}D$ iff $(s, Dt) = 0$ for all $t$ iff $(Ds,t) = 0$ for all $t$ iff $Ds = 0$; in finite dimensions the orthogonal complement of the kernel is exactly the image, and both are invariant under $D$ because $D$ commutes with itself and preserves its kernel.

**Corollary (the index is an obstruction of the kernel alone).** If the module carries a chirality grading $\gamma$ with $\gamma^{2} = 1$, $\gamma^{*} = \gamma$, and the operator is odd, $\gamma D = -D\gamma$, then $D$ interchanges the two chiral halves and the **index** $\operatorname{ind}(D^{+}) = \dim\ker D^{+} - \dim\ker D^{-}$ is the supertrace of $\gamma$ over $\ker D$. The computation of this integer from the geometry is the Atiyah–Singer theorem of Part IV; the Hermitian structure is what makes the index a difference of dimensions of positive definite spaces.

## The Finite-Dimensional Model

**Setting.** Take $S = \mathrm{Cl}(V,q)$ with the regular form $(x,y) = \mathrm{Sc}(x^{\dagger}y)$, and drop the derivative: the operator is the **Dirac element**

$$
D_{\mathrm{alg}} = \sum_{j} L_{e_j} ,
$$

the sum of the left multiplications by an orthonormal frame. This is the flat, massless model with no derivation, and every quantity is computable.

**Theorem.** The Dirac element is skew-adjoint, and its square is the Clifford Laplacian:

$$
D_{\mathrm{alg}}^{*} = -\,D_{\mathrm{alg}}, \qquad D_{\mathrm{alg}}^{2} = \Bigl(\sum_j q(e_j)\Bigr)\mathrm{id}, \qquad
(D_{\mathrm{alg}}x, D_{\mathrm{alg}}y) = -\Bigl(\sum_j q(e_j)\Bigr)(x,y).
$$

**Proof.** $L_{e_j}^{*} = L_{e_j^{\dagger}} = -L_{e_j}$, so $D_{\mathrm{alg}}^{*} = -\sum_jL_{e_j} = -D_{\mathrm{alg}}$. For the square, the cross terms $L_{e_i}L_{e_j} + L_{e_j}L_{e_i} = L_{e_ie_j + e_je_i}$ vanish for an orthonormal frame of a non-degenerate form, leaving $D_{\mathrm{alg}}^{2} = \sum_jL_{e_j}L_{e_j} = \sum_jL_{q(e_j)} = (\sum_jq(e_j))\mathrm{id}$; the form identity follows from the square and the skew-adjointness.

**Corollary (explicit spectrum and positivity).** In the negative definite case, where the dagger is positive, $\sum_jq(e_j) = -m$ and

$$
D_{\mathrm{alg}}^{2} = -m\,\mathrm{id}, \qquad D_{\mathrm{alg}}^{*}D_{\mathrm{alg}} = -D_{\mathrm{alg}}^{2} = m\,\mathrm{id} > 0 ,
$$

so $D_{\mathrm{alg}}$ is a skew-adjoint operator with purely imaginary spectrum $\{\pm i\sqrt m\}$, invertible, with trivial kernel; the real operator $iD_{\mathrm{alg}}$ is **self-adjoint** with spectrum $\{\pm\sqrt m\}$ and positive square $m\,\mathrm{id}$. The Dirichlet form $(D_{\mathrm{alg}}x, D_{\mathrm{alg}}x) = m\,(x,x)$ shows that the model is a "spectral gap" with gap $m$: on the flat definite algebra the Dirac element is invertible and its inverse has norm $1/\sqrt m$, so there are no harmonic spinors and the index vanishes.

**Remark (the sign bookkeeping).** The sign of $\sum_jq(e_j)$ is the whole content of the positivity: the Dirac element squares to the **negative** of the sum of the squares of the frame, which is positive exactly in the definite case, and the Hermitian square $D^{*}D$ is the positive operator $-\sum_jq(e_j)\,\mathrm{id}$. For an indefinite form the sum can vanish — the isotropic case — and the Dirac element is then nilpotent up to the metric, which is the algebraic form of the failure of ellipticity.

**Example (the biquaternion algebra).** In $\mathbb{B} = \mathbb{C}\otimes\mathbb{H}$ with the frame $e_1,e_2,e_3$ of square $-1$, the Dirac element $D_{\mathrm{alg}} = L_{e_1}+L_{e_2}+L_{e_3}$ is skew-adjoint with $D_{\mathrm{alg}}^{2} = -3\,\mathrm{id}$ and $D_{\mathrm{alg}}^{*}D_{\mathrm{alg}} = 3\,\mathrm{id}$; the real operator $iD_{\mathrm{alg}}$ is self-adjoint with spectrum $\{\pm\sqrt3\}$ and the eigen-spinors form an orthonormal basis of $\mathbb{B}$ for the form $\mathrm{Sc}(x^{\dagger}y)$. This is the smallest definite model with a non-abelian spin group, and it realises the spectral gap explicitly.

## Summary

A **Dirac operator** $D = \sum_j\rho(e_j)\partial_j$ on a Hermitian Clifford module is the product of two skew-adjoint factors, the Clifford coefficient $\rho(e_j)^{*} = -\rho(e_j)$ and the first-order operator $\partial_j^{*} = -\partial_j$; the two sign flips cancel and $D^{*} = D$, so $D$ is **formally self-adjoint** with respect to the module form, with real spectrum and orthogonal eigenspinors. Its **Hermitian square** is positive, $(D^{2}s,s) = \lVert Ds\rVert^{2}\ge0$, its kernel is the space of **harmonic spinors** with a positive definite form, and the module splits orthogonally as $S = \ker D\oplus\operatorname{im}D$; with a chirality grading the operator is odd and the index is the supertrace of the chirality on the kernel, computed geometrically by the Atiyah–Singer theorem of Part IV.

The **finite-dimensional model** is the Dirac element $D_{\mathrm{alg}} = \sum_jL_{e_j}$ on the regular module, which is skew-adjoint with $D_{\mathrm{alg}}^{2} = (\sum_jq(e_j))\mathrm{id}$; in the negative definite case $D_{\mathrm{alg}}^{2} = -m\,\mathrm{id}$, the Hermitian square $D_{\mathrm{alg}}^{*}D_{\mathrm{alg}} = m\,\mathrm{id}$ is positive, the spectrum of $D_{\mathrm{alg}}$ is $\{\pm i\sqrt m\}$, the operator is invertible with no harmonic spinors, and the real self-adjoint operator $iD_{\mathrm{alg}}$ has the spectral gap $m$. The biquaternion algebra with the frame of square $-1$ realises the model with gap $3$ and a non-abelian spin group. The analytic theory — domains, closures, essential self-adjointness, the spectrum of the flat model, the compact resolvent and the index — is *Dirac Differential Operators*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho$, $(\cdot,\cdot)$ | One-sided Clifford action and module form |
| $D = \sum_j\rho(e_j)\partial_j$ | Dirac operator, $\partial_j^{*}=-\partial_j$ |
| $D^{*} = D$ | Formal self-adjointness |
| $(D^{2}s,s) = \lVert Ds\rVert^{2}\ge0$ | Positivity of the Hermitian square |
| $\ker D$ | Harmonic spinors |
| $S = \ker D\oplus\operatorname{im}D$ | Hodge splitting by the kernel |
| $\gamma$, $\operatorname{ind}(D^{+})$ | Chirality grading and index |
| $D_{\mathrm{alg}} = \sum_jL_{e_j}$ | Finite-dimensional Dirac element |
| $D_{\mathrm{alg}}^{2} = (\sum_jq(e_j))\mathrm{id}$ | Clifford Laplacian |
| $D_{\mathrm{alg}}^{*}D_{\mathrm{alg}} = -\sum_jq(e_j)\,\mathrm{id}$ | Positive Hermitian square of the model |

## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Dirac operator on a Hermitian Clifford module, the positivity of the square and the space of harmonic spinors.
- Nicole Berline, Ezra Getzler and Michèle Vergne, *Heat Kernels and Dirac Operators*, Grundlehren der mathematischen Wissenschaften 298 (Springer, 1992), for the Weitzenböck formula, the positivity of the square and the Hodge-type splitting.
- Mikio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for self-adjoint operators, their spectra and the positivity of $D^{*}D$.
- Richard S. Palais, *The Atiyah–Singer Index Theorem*, Lecture Notes in Mathematics 835 (Springer, 1995), for the index of the chiral part of a Dirac operator and its computation from the geometry.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the Dirac element, its square and the explicit low-dimensional models.
