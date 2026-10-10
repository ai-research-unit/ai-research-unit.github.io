# __Congruence and the Stabiliser of a Form__

## Introduction

Forms of the same kind on the same space are compared by **congruence**: a change of basis carries a form to another form, and the pair (form, basis) is compared with the pair (form, other basis) by the change of coordinates. In the layer of *Sesqualgebras with a Form* the comparison is the action

$$
h \longmapsto h_{C}, \qquad h_{C}(x,y) = h(Cx, Cy) \qquad (C \text{ invertible}),
$$

of the group of units of the algebra on the set of the forms of the layer. The action is the congruence action, its orbits are the **congruence classes**, and its **stabiliser** of $h$ is exactly the unitary group $U(A,h)$ of *Isometries and the Unitary Group of a Form*. This article proves the last statement and organises the classification that the action produces.

The substance is threefold. The Gram matrix of $h_{C}$ in a basis is $C^{\dagger}GC$, the transform of the Gram matrix of $h$; the determinant is multiplied by a norm, so the non-degeneracy and the rank are invariants of the class. The stabiliser of $h$ is the unitary group, because the equation $h(Cx,Cy) = h(x,y)$ is the isometry equation and nothing else. And the classification of the classes is the classical classification of the forms: over $\mathbb{R}$ the complete invariant is the signature (Sylvester's law of inertia), over $\mathbb{C}$ it is the signature for a Hermitian form and the rank for a complex bilinear form, and over a general field with an involution it is the Witt class, whose group is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint* and *Witt's Theorems*.

The matrix equations are those of *Isometries and Unitary Operators of a Form*; the signatures are *The Indefinite Case and the Signature* and *Real Forms and the Signature*; the transport of the operators along the congruence is the conjugation that *The Unitary Group of a Form and Its Lie Algebra* reads infinitesimally. Throughout, $(A,*,h)$ is a sesqualgebra with a form with $h$ nonsingular, the operators are the invertible $R$-linear endomorphisms of $A$ in the multiplicative reading of the Gram-matrix formulas, and $G$ is the Gram matrix of $h$ in a fixed basis.

## The Congruence Action

**Definition.** For an invertible operator $C$ the **congruent form** of $h$ is $h_{C}(x,y) = h(Cx, Cy)$; the set $\{h_{C} : C$ invertible$\}$ is the congruence class of $h$, and its stabiliser is the **stabiliser** of $h$, $\operatorname{Stab}(h) = \{C \text{ invertible} : h_{C} = h\}$.

**Proposition.** The form $h_{C}$ is $\varsigma$-sesquilinear and Hermitian whenever $h$ is, the assignment $C \mapsto h_{C}$ is a right action of the group of the units, $h_{CD} = (h_{D})_{C}$, and the non-degeneracy is preserved.

**Proof.** Sesquilinearity: $h_{C}(\lambda x, y) = h(C(\lambda x), Cy) = h(\lambda Cx, Cy) = \lambda h_{C}(x,y)$, and the same on the right. Hermitian: $h_{C}(y,x) = h(Cy,Cx) = \varsigma(h(Cx,Cy)) = \varsigma(h_{C}(x,y))$. The action: $h_{CD}(x,y) = h(CDx,CDy) = h_{D}(Cx,Cy) = (h_{D})_{C}(x,y)$. Non-degeneracy: if $h_{C}(x,y) = 0$ for every $y$ then $h(Cx, Cy) = 0$ for every $y$, and $C$ being onto, $h(Cx, z) = 0$ for every $z$, so $Cx = 0$ and $x = 0$.

**Proposition (the Gram matrix).** In a basis with the Gram matrix $G$ and the multiplication reading of the operators,

$$
G_{C} = C^{\dagger}GC, \qquad \det G_{C} = \varsigma(\det C)\det(G)\det C .
$$

**Proof.** $(G_{C})_{ij} = h_{C}(e_{i},e_{j}) = h(Ce_{i},Ce_{j})$ and the coordinates of $Ce_{i}$ are the $i$-th column of $C$, so $G_{C} = C^{\dagger}GC$; the determinant formula is the multiplicativity of the determinant and the semilinearity of the dagger.

**Corollary.** The non-degeneracy and the rank of the form are invariants of the congruence class, and the determinant changes by the norm $\varsigma(\det C)\det C$ of the change of basis.

## The Stabiliser Is the Unitary Group

**Proposition.** The stabiliser of $h$ is the unitary group of the form:

$$
\operatorname{Stab}(h) = \{C \text{ invertible} : h(Cx,Cy) = h(x,y) \ \text{for all } x,y\} = U(A,h) .
$$

**Proof.** The two defining conditions are the same equation; the elements of the left-hand set are the invertible isometries of $h$, which is the unitary group by *Isometries and the Unitary Group of a Form*. In the multiplication reading the condition is $C^{\dagger}GC = G$ of *Isometries and Unitary Operators of a Form*, which is the same equation in coordinates.

**Corollary.** The congruence action is transitive on the forms of a fixed signature and free on the classes up to the stabiliser; the class of $h$ is the quotient of the group of units by $U(A,h)$, and the conjugates of the unitary group along the class are the unitary groups of the congruent forms:

$$
U(A,h_{C}) = C^{-1}\,U(A,h)\,C .
$$

**Proof.** The last identity is the transport of the isometry condition: $D$ is an isometry of $h_{C}$ iff $h(CDx,CDy) = h(Cx,Cy)$ iff $C^{-1}DC$ is an isometry of $h$.

## The Congruence Classification

**Theorem (Sylvester's law of inertia).** Over $\mathbb{R}$ two non-degenerate symmetric or Hermitian forms are congruent exactly when they have the same signature $(p,q)$; the signature is the complete invariant of the congruence class.

**Proof.** The theorem is the classical law of inertia, proved by the simultaneous reduction of the form to a diagonal shape with $\pm 1$ entries and by the invariance of the numbers of the positive and the negative squares under a change of basis; the algebraic proof over an ordered field, and the transfer to the Hermitian case, are *The Indefinite Case and the Signature*.

**Proposition (the Hermitian case over $\mathbb{C}$).** Over $\mathbb{C}$ two non-degenerate Hermitian forms are congruent exactly when they have the same signature: Sylvester's law of inertia holds verbatim, because the congruence $G \mapsto C^{\dagger}GC$ scales a diagonal entry by $\varsigma(z)z = |z|^{2}$, a positive real number, and the signs are therefore invariant.

**Proof.** The diagonal of the conjugate form is read in the same basis: if $h(z,z) > 0$ for all $z$ then $h_{C}(z,z) = h(Cz,Cz) > 0$ as well, so the number of the positive squares cannot decrease along the class, and by symmetry it cannot increase either; the two numbers are invariant. In particular $\operatorname{diag}(1,-1)$ is **not** congruent to $\operatorname{diag}(1,1)$: the change of basis $C = \operatorname{diag}(1,\mathrm{i})$ gives $C^{\dagger}\operatorname{diag}(1,-1)C = \operatorname{diag}\bigl(1,\varsigma(\mathrm{i})\cdot(-1)\cdot\mathrm{i}\bigr) = \operatorname{diag}(1,(-\mathrm{i})(-1)\mathrm{i}) = \operatorname{diag}(1,-1)$, fixed and not sent to the positive form.

**Proposition (the bilinear case over $\mathbb{C}$).** For a **complex bilinear** symmetric form, by contrast, the congruence uses the transpose, the sign can be changed and the complete invariant is the rank: under $C = \operatorname{diag}(1,\mathrm{i})$ one has $C^{T}\operatorname{diag}(1,1)C = \operatorname{diag}\bigl(1,\mathrm{i}^{2}\bigr) = \operatorname{diag}(1,-1)$, and every non-zero complex number is a square, so the diagonal entries of any non-degenerate form can be scaled to $1$ and the only invariant left is the rank.

**Proof.** The computation $C^{T}\operatorname{diag}(1,1)C = \operatorname{diag}(1,-1)$ is the displayed one; a diagonal matrix $\operatorname{diag}(d_{1},\dots,d_{n})$ with $d_{i} \neq 0$ is congruent to the identity through $\operatorname{diag}(c_{1},\dots,c_{n})$ with $c_{i}^{2} = d_{i}^{-1}$, which exists because $\mathbb{C}$ is closed under square roots. The two propositions together are the reason the layer distinguishes the Hermitian from the bilinear reading of the same diagonal matrix.

**Corollary.** Over a general field with an involution the classification is by the **Witt class**: two forms are congruent when they have the same Witt index and the same anisotropic part, and the classes form the Witt group of the layer, *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*; the cancellation that makes the decomposition invariant is *Witt's Theorems*.

## The Transport of the Operators

**Proposition.** Let $T$ be an operator and $C$ invertible; then $C^{-1}TC$ is an operator on $A$ and

$$
\bigl(C^{-1}TC\bigr)^{*} = C^{-1}T^{*}C
$$

for the adjoint with respect to $h$ on the left and with respect to $h_{C}$ on the right; consequently the congruence transports the self-adjoint, the skew-adjoint and the unitary operators of the form to the corresponding operators of the congruent form.

**Proof.** $h_{C}(C^{-1}TCx, y) = h(TCx, Cy) = h(Cx, T^{*}Cy) = h_{C}(x, C^{-1}T^{*}Cy)$, which identifies the adjoint of $C^{-1}TC$ for $h_{C}$ with $C^{-1}T^{*}C$. The sign conditions are invariant under conjugation, since $\pm$ is central, and the isometry condition is preserved by the last corollary of the previous section.

**Corollary.** The spectra of the transported operators, their positivity and their polar decomposition are invariants of the congruence class, and their theory is Part II: *Unitary Equivalence and Congruence of Operators with Hermitian Adjoint* and *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*.

## Examples

### The Matrices

On $M_n(\mathbb{C})$ with the trace form the congruence is $G \mapsto C^{\dagger}GC$, and the signature classifies over $\mathbb{R}$; over $\mathbb{C}$ the Hermitian forms are still classified by the signature, while a complex bilinear form of the same Gram matrix is classified only by its rank. The stabiliser of the identity Gram matrix is $U(n)$. The smallest cases are

$$
C=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad C^{\dagger}I_2C=\begin{pmatrix}1&1\\1&2\end{pmatrix},\qquad C^{\dagger}\begin{pmatrix}1&0\\0&-1\end{pmatrix}C=\begin{pmatrix}1&1\\1&0\end{pmatrix},
$$

so the same congruence carries the definite form to the first Gram matrix, of determinant $1$ and signature $(2,0)$, and the indefinite one to the second, of determinant $-1$ and signature $(1,1)$.

### The Indefinite Form

On $\mathbb{R}^{4}$ with the form of signature $(1,3)$ the congruence class is the Lorentz class, its stabiliser is $\operatorname{O}(1,3)$, and the transport $C^{-1}TC$ is the change of the Lorentz frame of the physics articles.

### The Biquaternion Algebra

On $\mathbb{B}$ the congruence of the plain and the quaternionic forms, their signatures and their stabilisers are the biquaternion computations of *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form* and *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*.

## Summary

- **Congruence** is the action $h \mapsto h_{C}$, $h_{C}(x,y) = h(Cx,Cy)$, of the invertible operators on the forms; it preserves the sesquilinearity, the Hermitian property and the non-degeneracy.
- The Gram matrix transforms as $G \mapsto C^{\dagger}GC$, and the determinant by the norm $\varsigma(\det C)\det C$; the rank and the non-degeneracy are invariants of the class.
- The **stabiliser** of $h$ is exactly the unitary group $U(A,h)$, and the unitary groups of the congruent forms are conjugate: $U(A,h_{C}) = C^{-1}U(A,h)C$.
- Over $\mathbb{R}$ the class is the **signature** (Sylvester); over $\mathbb{C}$ a Hermitian form is classified by the signature as well, while a complex bilinear form is classified by the rank; over a general field with an involution the class is the **Witt class**.
- The congruence transports the operators by $T \mapsto C^{-1}TC$ and the adjoint by $T^{*} \mapsto C^{-1}T^{*}C$, so the self-adjoint, the skew-adjoint and the unitary operators are carried to the corresponding operators of the congruent form.
- The spectra, the positivity and the polar decomposition of the transported operators are Part II.

## Summary of Notation

| symbol | meaning |
|---|---|
| $h_{C}$ | the congruent form $h(Cx,Cy)$ |
| $\operatorname{Stab}(h)$ | the stabiliser of $h$, equal to $U(A,h)$ |
| $G$, $G_{C}$ | the Gram matrices of $h$ and of $h_{C}$ |
| $(p,q)$ | the signature of a form over an ordered field |
| $C^{-1}TC$ | the transported operator |

## Further Reading

- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for congruence, the Witt group and the Witt decomposition.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for congruence over a ring with an involution and the unitary group as a stabiliser.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for Sylvester's law and the classification of the forms over a field.
