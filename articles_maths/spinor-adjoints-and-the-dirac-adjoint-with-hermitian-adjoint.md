
# __Spinor Adjoints and the Dirac Adjoint with Hermitian Adjoint__

## Introduction

A Hermitian Clifford module carries a form for which the Clifford action is self-adjoint. Attached to the form are two further structures that the physical literature names separately. The first is the **spinor adjoint**: the conjugate-linear identification of the module with its dual that the form induces, $s\mapsto(s,\cdot)$, which is the unique Clifford-equivariant pairing of the module with itself up to a scalar and is the algebraic object every spin-invariant bilinear form is built from. The second is the **Dirac adjoint**: the pairing of two spinors obtained by inserting a fixed vector $v$ before the form, $s,t\mapsto \mathrm{Sc}(s^{\dagger}v t)$, written in the physical normalisation as $\psi^{\dagger}v_0$, with $v_0$ the time-like vector, and whose scalar part $\psi^{\dagger}v_0\psi$ is the invariant mass term. This article treats both, together with the way they repair the isotropy of the naive scalar form on a spinor module and the way they interact with the self-adjointness of the Dirac operator.

The two constructions are the resolution of a difficulty raised in *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*: the restriction of the scalar form $\mathrm{Sc}(s^{\dagger}t)$ to a minimal left ideal is invariant but **totally isotropic** whenever $\pi^{\dagger}\pi = 0$, so the naive form is not the Hermitian structure of a general spinor module. The spinor adjoint supplies the missing non-degeneracy: it is the choice of a self-adjoint idempotent, equivalently of a Hermitian form on the module of the correct type. The type — orthogonal, symplectic or unitary — is exactly the type of the involution of the algebra, and the classification of the possible forms is the classification of Hermitian forms over a division algebra with involution.

The Clifford action and the module form are *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*; the adjoint of the one-sided action is *The Adjoint of the One-Sided Action with Hermitian Adjoint*; the Dirac operator and its Hermitian square are *Dirac Operators with Hermitian Adjoint*; the reality structures and the real, complex and quaternionic trichotomy are *Real Spinors and Reality Conditions with Inner Conjugation*; the Hermitian forms over an involution ring and the uniqueness of the invariant form are *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint* and *Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint*; the spinor module and the idempotents are *Peirce Carriers and Inner Conjugation*; the unitary slice is *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*; and the physical reading of the Dirac adjoint is in the physics menu.

## The Adjoint Module and the Spinor Adjoint

### The Adjoint Module

**Definition.** Let $S$ be a left Clifford module and let $A$ be the scalar field with involution $\sigma$. The **adjoint module** (the dual module) is $S^{*} = \mathrm{Hom}_A(S,A)$ with the action

$$
(x\cdot\varphi)(s) = \varphi\bigl(x^{\dagger}\cdot s\bigr) .
$$

**Proposition.** With this action $S^{*}$ is a Clifford module, and the assignment $x\mapsto\rho(x^{\dagger})^{T}$ is the corresponding action on the dual; moreover the action is the transpose of the adjoint action, so that the natural pairing $\langle\varphi,s\rangle = \varphi(s)$ satisfies

$$
\langle x\cdot\varphi, s\rangle = \langle \varphi, x^{\dagger}\cdot s\rangle .
$$

**Proof.** The pairing identity is the definition; the module axioms for $S^{*}$ are those of $\rho$ transported by the $*$-property $\rho(x^{\dagger}) = \rho(x)^{*}$ of *The Adjoint of the One-Sided Action with Hermitian Adjoint*, and the associativity follows.

### The Spinor Adjoint

**Theorem (the form is the spinor adjoint).** A Hermitian form on $S$ for which the action is self-adjoint is the same thing as a $\sigma$-semilinear map

$$
\boxed{\;J : S \longrightarrow S^{*}, \qquad J(s) = (s,\cdot), \qquad \langle J(s), t\rangle = (s,t)\;},
$$

that intertwines the action with the adjoint action,

$$
J\bigl(x\cdot s\bigr) = x\cdot J(s) ,
$$

and whose associated sesquilinear form is Hermitian, $J(s)(t) = \sigma\bigl(J(t)(s)\bigr)$. The map $J$ is called the **spinor adjoint**.

**Proof.** The adjointness axiom $(x\cdot s,t) = (s,x^{\dagger}\cdot t)$ becomes $\langle J(xs), t\rangle = \langle J(s), x^{\dagger}t\rangle = \langle x\cdot J(s), t\rangle$ for all $t$, that is $J(xs) = x\cdot J(s)$; Hermiticity of the form is the second condition.

**Corollary (uniqueness).** On an irreducible Clifford module over a simple algebra the spinor adjoint is unique up to a scalar in $A^{\sigma}$, by the Schur theorem of *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*; it is the module-theoretic form of the statement that a spinor inner product is well defined without further choices. On the regular module the uniqueness fails, with the multiplicity of the module as the dimension of the space of such adjoints.

**Remark (the type of the involution).** The spinor adjoint $J$ and the form it defines have a **type**: the form is symmetric, alternating or Hermitian in the sense of *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, and the type is determined by the type of the involution of the algebra — orthogonal, symplectic or unitary — and by the division algebra over the module. Over $\mathbb{C}$ with an antilinear involution the type is the Hermitian one and the reality of the underlying module is the real/complex/quaternionic trichotomy of *Real Spinors and Reality Conditions with Inner Conjugation*; over $\mathbb{R}$ the three types are the three possibilities. The classification of the possible types is part of the classification of Hermitian forms over a division algebra with involution and is, as in the unitary Witt group, the invariant that makes the spinor form well defined.

## The Isotropy of the Naive Form and Its Repair

**Proposition (the naive restriction is isotropic).** Let $\pi$ be a primitive idempotent with $\pi^{\dagger}\pi = 0$, as for $\pi = \tfrac12(1+e)$ with $e^2 = 1$ in the standard convention. Then the restriction of $\mathrm{Sc}(s^{\dagger}t)$ to the minimal left ideal $\mathrm{Cl}\,\pi$ is zero, so the naive scalar form does not give the Hermitian structure of the module.

**Proof.** This is the verified computation of *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint* in $\mathrm{Cl}_{1,1}(\mathbb{R})$: the Gram matrix on the two-dimensional ideal is the zero matrix.

**Theorem (the repair).** The Hermitian structure of a spinor module is obtained from the **spinor adjoint** of a self-adjoint idempotent, equivalently from a Hermitian form of the correct type on the irreducible module, and not from the naive restriction of the scalar form. In the definite case, where the dagger is a positive involution, the irreducible module of the full matrix algebra carries a positive definite Hermitian form and the spinor adjoint is a positive definite inner product; in the split case the invariant form is isotropic or hyperbolic and the idempotent is not self-adjoint.

**Proof.** In the definite case the algebra is a full matrix algebra over a division algebra with a positive involution, its matrix units are self-adjoint, and the form $\mathrm{Sc}(s^{\dagger}t)$ is positive definite on the column module; this is the positivity theorem of *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint* and the structure theory of *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*. In the split case the involution is hyperbolic and the idempotent $\tfrac12(1+e)$ with $e^2=1$ satisfies $\pi^{\dagger}\pi=0$, so the restriction is isotropic; the invariant form exists but is not definite.

**Remark.** So the spinor adjoint is not an extra structure added to a spinor module; it is the same data as the Hermitian form, read as a map to the dual. The "choice" of spinor inner product is the choice of a self-adjoint idempotent, and the two are unique up to a scalar on an irreducible module.

## The Dirac Adjoint

### The Pairing with a Vector

**Definition.** Let $v \in V$ be a non-isotropic vector. The **Dirac adjoint pairing** is

$$
\beta_{v}(s,t) = \mathrm{Sc}\bigl(s^{\dagger}\,v\,t\bigr) = \bigl\langle J(s), v\,t\bigr\rangle ,
$$

the form of the spinor adjoint with the vector $v$ inserted before the second spinor. In the physical normalisation one writes $\bar s = s^{\dagger}v$ and $\beta_{v}(s,t) = \mathrm{Sc}(\bar s\, t)$, so that $\bar s\, s = \beta_{v}(s,s)$ is the invariant "mass".

**Proposition (Hermiticity is governed by $v_{\dagger} = \pm v$).** For a vector $v$, $v_{\dagger} = -v$, and consequently

$$
\beta_{v}(t,s) = -\,\overline{\beta_{v}(s,t)} ,
$$

so $\beta_{v}$ is **skew-Hermitian** for every non-isotropic vector $v$, and $i\beta_{v}$ is Hermitian. If $v$ is central and self-adjoint, then $\beta_{v}$ is Hermitian; the sign is the sign of $v_{\dagger}v$.

**Proof.** $\overline{\beta_{v}(s,t)} = \mathrm{Sc}\bigl((s^{\dagger}v t)^{\dagger}\bigr) = \mathrm{Sc}\bigl(t^{\dagger}v_{\dagger} s\bigr) = -\mathrm{Sc}\bigl(t^{\dagger}v s\bigr) = -\beta_{v}(t,s)$, using $v_{\dagger} = -v$ and the cyclicity of the scalar part.

**Theorem (non-degeneracy and invariance).** For non-isotropic $v$ the pairing $\beta_{v}$ is non-degenerate, and it is invariant under the stabiliser of $v$ in the unitary slice:

$$
\boxed{\;u^{\dagger}v u = v \ \Longrightarrow \ \beta_{v}(u\cdot s, u\cdot t) = \beta_{v}(s,t)\;} .
$$

**Proof.** Non-degeneracy follows because $\mathrm{Sc}(s^{\dagger}v t)$ is $\mathrm{Sc}$ composed with the invertible multiplications by $v$ and by the dagger; invariance is $\beta_{v}(us,ut) = \mathrm{Sc}(s^{\dagger}u^{\dagger}v u t) = \mathrm{Sc}(s^{\dagger}v t)$ for $u^{\dagger}v u = v$.

**Corollary (the physical Dirac adjoint).** In the Lorentzian case the stabiliser of a time-like $v_0$ is the maximal compact subgroup $\mathrm{Spin}(m)\subseteq\mathrm{Spin}(1,m)$, and $\beta_{v_0}$ is the $\mathrm{Spin}(m)$-invariant skew-Hermitian pairing whose normalisation by $i$ and by $v_0^{2}$ gives the Hermitian form of the quantum theory; the object $\psi^{\dagger}v_0$ is the Dirac adjoint of the physics literature, and the Lorentz-invariant bilinear $\psi^{\dagger}v_0\chi$ is $\beta_{v_0}$. This is the reason the invariant pairing of the spinor module is indefinite while the form used for the Hilbert space is positive definite on the maximal compact part. The physical reading of $\psi^{\dagger}v_0\psi$, of the current and of the mass term is in the physics menu and is not used here.

### The Dirac Adjoint and the Dirac Operator

**Theorem (adjointness of the Dirac operator for the Dirac pairing).** Let the frame be orthogonal to $v$, so that $v$ anticommutes with each $e_j$, and let $D$ be self-adjoint or skew-adjoint for the module form, $D^{*} = \varepsilon D$ with $\varepsilon = \pm1$. Then

$$
\boxed{\;\beta_{v}(D\cdot s, t) = -\,\varepsilon\,\beta_{v}(s, D\cdot t)\;} .
$$

In particular, an operator that is **skew**-adjoint for the module form $(\varepsilon = -1)$ is self-adjoint for the Dirac pairing, and an operator that is **self**-adjoint for the module form $(\varepsilon = +1)$ is skew-adjoint for the Dirac pairing.

**Proof.** $\beta_{v}(Ds,t) = (Ds,v t) = (s, D^{*}v t) = \varepsilon\,(s, Dv t) = \varepsilon\,(s, -v D t) = -\varepsilon\,(s,v D t) = -\varepsilon\,\beta_{v}(s,Dt)$, using the definition $\beta_{v}(s,t) = (s,v t)$ with $(\cdot,\cdot)$ the module form, the adjointness $D^{*} = \varepsilon D$, and the anticommutation $v e_j = -e_jv$ which gives $v D = -Dv$ so that $Dv = -v D$.

**Corollary (the finite-dimensional model and the PDE model).** In the finite-dimensional model of *Dirac Operators with Hermitian Adjoint*, $D_{\mathrm{alg}} = \sum_jL_{e_j}$ is skew-adjoint, $\varepsilon = -1$, so it is **self-adjoint** for the Dirac pairing; in the PDE model $D = \sum_j\rho(e_j)\partial/\partial x_j$ is self-adjoint, $\varepsilon = +1$, so it is **skew-adjoint** for the Dirac pairing. Both were checked by computation, and the two cases are the two signs of $\varepsilon$.

**Remark.** The $v$-twisted pairing is the one whose scalar part $\bar s\,t$ is the invariant bilinear of the physics, and the sign in front of the adjointness is the reason the Dirac adjoint is introduced: the pairing with the spinor adjoint alone is Hermitian, while the physical bilinear is the $v$-twisted pairing, whose sign structure differs by the self- or skew-adjointness of the operator. The analysis of the operator is *Dirac Operators with Hermitian Adjoint*; what the Dirac adjoint adds is the pairing.

## Worked Cases

### The Split Case: the Isotropy Repaired

In $\mathrm{Cl}_{1,1}(\mathbb{R})$ with $\vec e_x^{2} = 1$, $\vec e_y^{2} = -1$, let $\pi = \tfrac12(1+\vec e_x)$; the naive form $\mathrm{Sc}(s^{\dagger}t)$ on $\mathrm{Cl}\pi$ is zero, as computed, while the spinor adjoint of the module $\mathbb{R}^2$ with the hyperbolic form $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ is non-degenerate and isotropic: the module is a hyperbolic plane, its spinor adjoint pairs the two isotropic lines, and the "self-adjoint idempotent" is $E_{11}$ of the matrix model, which is self-adjoint for the **transpose** involution and not for the Clifford dagger. The example shows that the type of the involution, not the algebra alone, decides whether the spinor form is definite.

### The Definite Case: the Positive Spinor Form

In $\mathrm{Cl}_{0,2}(\mathbb{R}) = \mathbb{H}$ with the dagger positive, the algebra is a division algebra and has no minimal left ideal; the regular module with the form $\mathrm{Sc}(x^{\dagger}y) = \sum_\mu|Q_\mu|^{2}$ is positive definite, the spinor adjoint is the identity identification of $\mathbb{H}$ with its dual for that form, and there is no isotropic idempotent. The Dirac operator built from the frame $\vec e_x,\vec e_y$ has $D^{*} = -D$ and $D^{*}D = 2\,\mathrm{id}$, so it is invertible with no harmonic spinors, as in *Dirac Operators with Hermitian Adjoint*.

### The Lorentzian Case: the Dirac Adjoint

In $\mathrm{Cl}_{1,3}(\mathbb{R})$ with $\vec e_x^{2} = 1$ and $\vec e_y^{2} = \vec e_z^{2} = e_4^{2} = -1$, the vector $v_0 = \vec e_x$ is time-like, and $\beta_{v_0}(s,t) = \mathrm{Sc}(s^{\dagger}\vec e_xt)$ is a non-degenerate skew-Hermitian pairing on the 16-dimensional regular module, invariant under the subgroup of the slice that stabilises $\vec e_x$, which is generated by the rotations $\exp(\theta\,e_ie_j)$ in the space-like directions. This is computed: the pairing is skew-Hermitian, $i\beta_{v_0}$ is Hermitian, the form is non-degenerate, and the stabiliser of $\vec e_x$ preserves it. The Lorentzian signature of the pairing, and the identification with the physics Dirac adjoint, are the indefinite counterpart of the definite case above.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame operator of the chirality $\Gamma$; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the basis operators span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

## Summary

The **spinor adjoint** is the conjugate-linear map $J : S\to S^{*}$, $J(s) = (s,\cdot)$, induced by the Hermitian form of a Hermitian Clifford module; it intertwines the action with the adjoint action, $J(x\cdot s) = x\cdot J(s)$, and on an irreducible module it is unique up to a scalar by Schur's lemma. It is the same data as the form, read as a map to the dual, and it is the algebraic object every spin-invariant bilinear form is built from; its **type** — symmetric, alternating or Hermitian — is determined by the type of the involution of the algebra and by the division algebra over the module, which is the real/complex/quaternionic trichotomy in the complex case.

The naive scalar form $\mathrm{Sc}(s^{\dagger}t)$ on a minimal left ideal with $\pi^{\dagger}\pi = 0$ is **totally isotropic**, as computed in $\mathrm{Cl}_{1,1}(\mathbb{R})$, and it is the **spinor adjoint of a self-adjoint idempotent** that repairs it: the definite case has a positive definite spinor form and the split case a hyperbolic one. The **Dirac adjoint** is the pairing $\beta_{v}(s,t) = \mathrm{Sc}(s^{\dagger}v t)$ with a non-isotropic vector $v$ inserted, written $\bar s = s^{\dagger}v$ in the physical normalisation; for a vector it is **skew-Hermitian** because $v_{\dagger} = -v$, so $i\beta_{v}$ is Hermitian, it is non-degenerate, and it is invariant under the stabiliser of $v$ in the unitary slice — in the Lorentzian case the maximal compact subgroup. The Dirac operator is formally self-adjoint for the spinor adjoint pairing and skew-adjoint for the $v$-twisted pairing, and the two pairings are the two faces of the Hermitian structure of a spinor module.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S^{*} = \mathrm{Hom}_A(S,A)$ | Adjoint module, action $(x\cdot\varphi)(s)=\varphi(x^{\dagger}s)$ |
| $J(s) = (s,\cdot)$, $\langle J(s),t\rangle = (s,t)$ | Spinor adjoint |
| $J(x\cdot s) = x\cdot J(s)$ | Equivariance of the spinor adjoint |
| $\beta_{v}(s,t) = \mathrm{Sc}(s^{\dagger}v t)$ | Dirac adjoint pairing |
| $\beta_{v}(t,s) = -\overline{\beta_{v}(s,t)}$ | Skew-Hermiticity for a vector $v$ |
| $u^{\dagger}v u = v$ | Stabiliser of $v$, preserving $\beta_{v}$ |
| $\bar s = s^{\dagger}v$ | Dirac adjoint (physical normalisation) |
| $\pi^{\dagger}\pi = 0$ | Isotropy of the naive ideal form |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](../articles_physics/why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the spinor inner product, the invariant bilinear forms and the self-adjointness of the Dirac operator.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the spinor adjoint, the Dirac adjoint and the explicit low-dimensional forms in the physics convention.
- James D. Bjorken and Sidney D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the Dirac adjoint, the invariant bilinear and the current in the physics normalisation.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the type of an involution, the Hermitian, symmetric and alternating forms over a division algebra with involution, and the classification that the spinor form's type obeys.
- Tsit-Yuen Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for the classification of forms over an involution ring and the Witt-theoretic invariants used here.
