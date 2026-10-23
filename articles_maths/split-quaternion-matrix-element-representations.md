
# __Split-Quaternion Matrix Element Representations__

## Introduction

This article treats the split-quaternion algebra as a matrix algebra. It exhibits the faithful representation by $2 \times 2$ real matrices, proves that it exists and is unique up to conjugacy, identifies the determinant with the split-quaternion norm and the trace with twice the scalar part, describes the image as a linear subspace of $M_2(\mathbb{R})$, and compares the situation with the quaternion algebra and with the eight-dimensional algebra, which admits no representation of this size.

The split-quaternion algebra and its multiplication table are assumed from *Split-Quaternion Algebra*; the matrix model $\mathsf{M}_2$ is defined here and its multiplicativity is verified here. The matrix algebra $M_n(\mathbb{R})$, its matrix units, its centre and the Skolem–Noether theorem that every automorphism of $M_n(k)$ over a field is inner are assumed from *Matrix Algebras*. The split-quaternion norm and its invertibility theory are assumed from *Split-Quaternion Norm and Invertibility*; the classification of the modules of the algebra belongs to *Split-Quaternion Element Representations*, which cites this article for the module of the model. Nothing physical is invoked.

## The Representation

**Definition.** A **matrix representation** of $\mathbb{H}_{\mathrm{s}}$ of degree $n$ is an injective unital algebra homomorphism

$$
\Psi : \mathbb{H}_{\mathrm{s}} \longrightarrow M_n(\mathbb{R}).
$$

The representation is **faithful** by definition, since injectivity is required; its **image** is the subalgebra $\Psi(\mathbb{H}_{\mathrm{s}})$.

**Definition.** The **defining representation** of $\mathbb{H}_{\mathrm{s}}$ is the isomorphism written $\mathsf{M}_2$. It converts a split quaternion into a $2 \times 2$ real matrix,

$$
\mathsf{M}_2 : \mathbb{H}_{\mathrm{s}} \longrightarrow M_2(\mathbb{R}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{R}$-linearity. The generators are assigned the matrices

$$
\mathsf{M}_2(1) = I, \quad \mathsf{M}_2(\vec e_x) = J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \quad
\mathsf{M}_2(\vec e_y) = K = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad
\mathsf{M}_2(\vec e_z) = D = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix},
$$

so that on a general element

$$
\boxed{\;
\mathsf{M}_2(q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z) = \begin{pmatrix} q_t - q_z & q_y - q_x \\ q_x + q_y & q_t + q_z \end{pmatrix}
\;}
$$.

The defining representation is the model in which every statement of this article is computed.

**The check.** The assignment is the right one because the four matrices multiply as the four generators do. Squaring the vector images,

$$
\mathsf{M}_2(\vec e_x)^2 = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}^2 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -\mathsf{M}_2(1), \qquad
\mathsf{M}_2(\vec e_y)^2 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}^2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \mathsf{M}_2(1),
$$

and the same gives $\mathsf{M}_2(\vec e_z)^2 = \mathsf{M}_2(1)$; so $\vec e_x^2 = -1$, $\vec e_y^2 = \vec e_z^2 = 1$ are reproduced. Multiplying the first two,

$$
\mathsf{M}_2(\vec e_x)\mathsf{M}_2(\vec e_y) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} = \mathsf{M}_2(\vec e_z),
$$

reproducing $\vec e_x\vec e_y = \vec e_z$. Those relations are the whole multiplication table of $\mathbb{H}_{\mathrm{s}}$, so the correspondence of bases is an isomorphism of algebras and not a formal analogy.

## Existence

**Theorem (Existence).** The split-quaternion algebra has a faithful real matrix representation of degree $2$, namely $\mathsf{M}_2$, and therefore

$$
\boxed{\;
\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})
\;}
$$

as real algebras.

**Proof.** By the multiplication table of *Split-Quaternion Algebra*, the linear map $\mathsf{M}_2$ is an algebra homomorphism, it is injective because the four generators have linearly independent images, and it is surjective because the domain and the target both have real dimension $4$. An isomorphism is in particular an injective unital homomorphism of degree $2$.

**Corollary (Dimension).** The least degree of a faithful real matrix representation of $\mathbb{H}_{\mathrm{s}}$ is $2$. Indeed a faithful representation of degree $n$ embeds a four-dimensional algebra into $M_n(\mathbb{R})$, whose dimension is $n^2$, so $n^2 \geq 4$, and $n = 1$ is impossible because $M_1(\mathbb{R})$ is commutative while $\mathbb{H}_{\mathrm{s}}$ is not; degree $2$ is attained.

**Proof.** The inequality is the dimension count, and the non-commutativity of $\mathbb{H}_{\mathrm{s}}$ excludes $n = 1$; the defining representation attains $n = 2$.

The existence theorem is the Clifford identification of the anchor article read as a representation statement: $\mathbb{H}_{\mathrm{s}} \cong \mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ by (*The Number Systems as Clifford Algebras*).

## Uniqueness up to Conjugacy

**Theorem (Uniqueness).** Let $\Psi : \mathbb{H}_{\mathrm{s}} \to M_2(\mathbb{R})$ be a unital algebra homomorphism. Then $\Psi$ is an isomorphism, and there is an invertible matrix $P$ with

$$
\Psi(\tilde q) = P \, \mathsf{M}_2(\tilde q) \, P^{-1} \qquad (\tilde q \in \mathbb{H}_{\mathrm{s}}).
$$

Thus the faithful representation of degree $2$ is unique up to conjugacy: any two such representations are equivalent.

**Proof.** The kernel of $\Psi$ is a two-sided ideal of $\mathbb{H}_{\mathrm{s}}$. The algebra is simple by (*Split-Quaternion Algebra*, §*The Centre and Simplicity*), so the kernel is either $0$ or the whole algebra; it is not the whole algebra because $\Psi(1) = I \neq 0$, so it is $0$ and $\Psi$ is injective. Both sides have dimension $4$, so $\Psi$ is bijective. Now $\Psi \circ \mathsf{M}_2^{-1}$ is an algebra automorphism of $M_2(\mathbb{R})$, and by the Skolem–Noether theorem of *Matrix Algebras* every automorphism of $M_2(\mathbb{R})$ is inner: there is $P \in GL_2(\mathbb{R})$ with $\Psi\mathsf{M}_2^{-1} = \operatorname{Int}_P$. Composing with $\mathsf{M}_2$ gives the displayed identity.

**Corollary (The Automorphisms of the Algebra).** Every automorphism of $\mathbb{H}_{\mathrm{s}}$ is obtained by conjugating by an invertible element:

$$
\operatorname{Aut}(\mathbb{H}_{\mathrm{s}}) \cong \mathrm{PGL}_2(\mathbb{R}), \qquad \alpha(\tilde q) = g \tilde q g^{-1} \quad (g \in \mathbb{H}_{\mathrm{s}}^{\times}).
$$

**Proof.** An automorphism $\alpha$ of $\mathbb{H}_{\mathrm{s}}$ corresponds to the inner automorphism $\mathsf{M}_2\alpha\mathsf{M}_2^{-1}$ of $M_2(\mathbb{R})$, which is inner by Skolem–Noether; transport back. Conversely every inner automorphism of the algebra is an automorphism, and two units $g, g'$ give the same automorphism exactly when $g' g^{-1}$ is central, which by (*Split-Quaternion Algebra*, §*The Centre and Simplicity*) means $g' = \lambda g$ with $\lambda \in \mathbb{R}^{\times}$.

## The Determinant and the Trace

**Theorem (Determinant and Trace).** For every split-quaternion $\tilde q$,

$$
\boxed{\;
\det \mathsf{M}_2(\tilde q) = \langle\tilde q\rangle_{\natural}, \qquad \operatorname{tr} \mathsf{M}_2(\tilde q) = 2 \operatorname{Sc}(\tilde q)
\;}
$$.

The determinant of the matrix model is the split-quaternion norm, a quadratic form of signature $(2,2)$, and the trace is twice the scalar part; the restriction of the trace to the vector subspace vanishes, so $\mathsf{M}_2(V)$ is the space of traceless matrices.

**Proof.** The determinant computation is (*Split-Quaternion Norm and Invertibility*, §*The Split-Quaternion Norm*). For the trace,

$$
\operatorname{tr}\mathsf{M}_2(q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z) = (q_t - q_z) + (q_t + q_z) = 2q_t = 2\operatorname{Sc}(\tilde q).
$$

The vanishing of the trace on $V$ is the case $q_t = 0$.

**Corollary (Formulas in the Model).** For every $\tilde q$,

$$
\det \mathsf{M}_2(\tilde{q}^{\natural}) = \det \mathsf{M}_2(\tilde q), \qquad \mathsf{M}_2(\tilde{q}^{\natural}) = \operatorname{adj}\mathsf{M}_2(\tilde q),
$$

and $\tilde q$ is a unit if and only if $\mathsf{M}_2(\tilde q)$ is invertible, in which case $\mathsf{M}_2(\tilde q^{-1}) = \mathsf{M}_2(\tilde q)^{-1} = \operatorname{adj}\mathsf{M}_2(\tilde q)/\det\mathsf{M}_2(\tilde q)$.

**Proof.** The conjugation is an involution of the algebra, so it preserves the split-quaternion norm: $\langle\tilde{q}^{\natural}\rangle_{\natural} = \tilde{q}^{\natural}\tilde q = \langle\tilde q\rangle_{\natural}$, and the first identity follows from $\det = N$. The second is the adjugate identity of (*Split-Quaternion Algebra*, §*The Conjugation*). The invertibility statement is the equality $\det\mathsf{M}_2 = N$ together with *Split-Quaternion Norm and Invertibility*, §*The Invertibility Criterion*.

## The Image as a Linear Subspace

**Theorem (The Image Is Everything).** The image of the defining representation is the whole matrix algebra:

$$
\mathsf{M}_2(\mathbb{H}_{\mathrm{s}}) = M_2(\mathbb{R}).
$$

There is no proper subalgebra of $M_2(\mathbb{R})$ of dimension $4$ other than $M_2(\mathbb{R})$ itself, so the image is not a proper linear subspace.

**Proof.** The image is a linear subspace of dimension $4$ inside the four-dimensional space $M_2(\mathbb{R})$.

The distinguished subspaces of the algebra correspond to the following subspaces of matrices.

| Subspace of $\mathbb{H}_{\mathrm{s}}$ | Image in $M_2(\mathbb{R})$ | Description |
|---|---|---|
| $S = \mathbb{R}\cdot 1$ | $\mathbb{R} I$ | the scalar matrices |
| $V = \operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$ | $\mathrm{SL}_2(\mathbb{R})$ | the traceless matrices |
| $\mathbb{D}_2 = \operatorname{span}\{1,\vec e_y\}$ | $\left\{\begin{pmatrix}p & q \\ q & p\end{pmatrix}\right\}$ | the symmetric matrices with equal diagonal |
| $\mathbb{D}_3 = \operatorname{span}\{1,\vec e_z\}$ | $\left\{\begin{pmatrix}p & 0 \\ 0 & q\end{pmatrix}\right\}$ | the diagonal matrices |
| $\mathbb{H}_{\mathrm{s}} \tilde\pi_1$, $\tilde\pi_1 \mathbb{H}_{\mathrm{s}}$ | $K_{\ell_w}$, $R_{\ell_v}$ | maximal isotropic subspaces |
| $\mathbb{H}_{\mathrm{s}} \tilde\pi_2$, $\tilde\pi_2 \mathbb{H}_{\mathrm{s}}$ | $K_{\ell_v}$, $R_{\ell_w}$ | maximal isotropic subspaces |

The last row is the dictionary of (*Split-Quaternion Zero Divisors*, §*The Two Families*), where $\ell_v$ and $\ell_w$ are the lines spanned by $(1,1)$ and $(1,-1)$ and the subspaces $R_\ell$, $K_\ell$ are the two families of maximal isotropic subspaces. The table shows that the algebra and the matrix algebra carry the same structure: the scalar part is the trace part, the vector part is the traceless part, the split-complex subalgebra $\mathbb{D}_3$ is the diagonal subalgebra, and the minimal ideals are the isotropic subspaces.

**Corollary (The Idempotents in the Model).** The idempotents of the algebra correspond to the idempotent matrices of rank one together with $0$ and $I$. In particular

$$
\mathsf{M}_2(\tilde\pi_1) = \tfrac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad
\mathsf{M}_2(\tilde\pi_2) = \tfrac12 \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix},
$$

two rank-one projections, and $\mathsf{M}_2(\tilde\pi_1) + \mathsf{M}_2(\tilde\pi_2) = I$ with $\mathsf{M}_2(\tilde\pi_1) \mathsf{M}_2(\tilde\pi_2) = 0$.

**Proof.** The images are computed from the formula for $\mathsf{M}_2$, and the identities are the images of the identities of (*Split-Quaternion Algebra*, §*The Idempotents*). The classification of idempotents is that of *Split-Quaternion Roots of Minus One*, §*The Relation to the Idempotents and to the Zero Divisors*.

## The Defining Module

The matrix algebra $M_2(\mathbb{R})$ acts on the column space $\mathbb{R}^2$, and through $\mathsf{M}_2$ this becomes an action of $\mathbb{H}_{\mathrm{s}}$.

**Definition.** The **defining module** of $\mathbb{H}_{\mathrm{s}}$ is the real vector space $\mathbb{R}^2$ with the action

$$
\tilde q \cdot v = \mathsf{M}_2(\tilde q) v, \qquad \tilde q \in \mathbb{H}_{\mathrm{s}}, \quad v \in \mathbb{R}^2 .
$$

**Theorem (Irreducibility).** The defining module is simple: it has no nonzero proper submodule. Consequently the defining representation is irreducible, and it is the unique irreducible representation of the algebra up to equivalence.

**Proof.** The submodules of the defining module are the $\mathsf{M}_2(\mathbb{H}_{\mathrm{s}})$-invariant subspaces of $\mathbb{R}^2$, and since $\mathsf{M}_2$ is surjective these are exactly the $M_2(\mathbb{R})$-invariant subspaces, that is, the subspaces stable under every $2 \times 2$ matrix. Let $W \neq 0$ be such a subspace and let $v = (v_1,v_2) \in W$ be nonzero. If $v_1 \neq 0$ then $E_{11}v = v_1 \vec e_x$ lies in $W$, so $\vec e_x \in W$, and then $E_{12}\vec e_x = \vec e_y \in W$; if $v_1 = 0$ then $v_2 \neq 0$ and the same argument with the roles exchanged gives $\vec e_y \in W$ and then $\vec e_x \in W$. Hence $W$ contains both standard basis vectors and is the whole space. The uniqueness is the classification of the modules of a simple algebra, treated in *Split-Quaternion Element Representations*.

The defining module is the concrete reason the matrix model is the right one: an eight-dimensional algebra cannot be a matrix algebra of this size, but a four-dimensional simple algebra is exactly a full matrix algebra over $\mathbb{R}$, and the module of the model is the module that the algebra realises.

## Comparison with the Quaternion Case and with $\mathbb{H}_{\mathbb{D}}$

### The Quaternion Case

The quaternion algebra has no faithful real matrix representation of degree $2$.

**Proposition.** There is no injective unital algebra homomorphism $\mathbb{H} \to M_2(\mathbb{R})$.

**Proof.** Such a homomorphism would embed the four-dimensional algebra $\mathbb{H}$ into the four-dimensional algebra $M_2(\mathbb{R})$, hence would be an isomorphism, so $\mathbb{H} \cong M_2(\mathbb{R})$; but $\mathbb{H}$ is a division algebra by *Quaternion Algebra* and $M_2(\mathbb{R})$ has zero divisors.

The quaternions do have a faithful representation by $2 \times 2$ **complex** matrices, obtained from the same Pauli-type assignment with $i$ in place of the real rotation matrix: the scalar extension $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{C} = \mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$, as recorded in *The Number Systems as Clifford Algebras*, and so the quaternions act on $\mathbb{C}^2$. Over $\mathbb{R}$ the least faithful representation is of degree $4$: no representation of degree $2$ or $3$ exists, and the regular representation of the algebra on itself, of real dimension $4$, is faithful. The difference from the split case is the difference between the two real forms of the same complex algebra: the definite form gives a division algebra with no real degree-two model, the indefinite form gives the matrix algebra, which is the degree-two model itself.

**Proposition (The Least Degree over $\mathbb{R}$).** The quaternion algebra has no faithful real matrix representation of degree $2$ or $3$.

**Proof.** Degree $2$ is excluded by the preceding proposition. For degree $3$, suppose $\mathbb{H}$ acts faithfully on $\mathbb{R}^3$. Choose $v \neq 0$. The map $\mathbb{H} \to \mathbb{R}^3$, $h \mapsto hv$, is injective: if $hv = 0$ with $h \neq 0$, then multiplying by the inverse of $h$ gives $v = 0$. Hence $\mathbb{R}^3$ contains a subspace isomorphic to $\mathbb{H}$, of real dimension $4$, which is impossible.

### The Absence of a Two-Dimensional Real Model for $\mathbb{H}_{\mathbb{D}}$

The eight-dimensional algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ of the notation table has no faithful $2 \times 2$ real matrix representation, and the obstruction is dimension alone.

**Proposition.** There is no injective unital algebra homomorphism $\mathbb{H}_{\mathbb{D}} \to M_2(\mathbb{R})$.

**Proof.** Such a homomorphism would embed a real vector space of dimension $8$ into one of dimension $4$, which is impossible for an injective linear map.

The algebra is treated later in Part V, under Split-Biquaternions; nothing of it is used here beyond its dimension, which is fixed by the notation table. Its faithful linear representations have degree at least $3$, since $3^2 = 9 \geq 8$, and the description of them belongs to the later category.

## Summary

The split-quaternion algebra has a faithful real matrix representation of degree $2$, the defining representation $\mathsf{M}_2(q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z) = \begin{pmatrix} q_t-q_z & q_y-q_x \\ q_x+q_y & q_t+q_z\end{pmatrix}$, and no faithful representation of lower degree. The representation is unique up to conjugacy: every unital algebra homomorphism $\mathbb{H}_{\mathrm{s}} \to M_2(\mathbb{R})$ is an isomorphism, and any two differ by conjugation by an invertible matrix. The automorphism group of the algebra is $\mathrm{PGL}_2(\mathbb{R})$, acting by inner automorphisms.

The determinant of the model is the split-quaternion norm $\langle\cdot\rangle_{\natural}$, of signature $(2,2)$, and the trace is twice the scalar part; the vector subspace is the traceless part, and conjugation is the adjugate. The image of the algebra is the whole of $M_2(\mathbb{R})$, and the distinguished subspaces of the algebra correspond to the scalar matrices, the traceless matrices, the diagonal subalgebra, the symmetric subalgebra, the minimal ideals and the two families of maximal isotropic subspaces. The defining module $\mathbb{R}^2$ is simple, and it is the unique irreducible module of the algebra.

The quaternion algebra has no faithful real degree-two representation, because an isomorphism with $M_2(\mathbb{R})$ would contradict its being a division algebra, although its complexification is $M_2(\mathbb{C})$; the eight-dimensional algebra has none either, by the dimension count alone, and its representations belong to the later category.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\Psi$ | a matrix representation of $\mathbb{H}_{\mathrm{s}}$ | this article |
| $\mathsf{M}_2$ | the defining representation, $\tilde q \mapsto \begin{pmatrix} q_t-q_z & q_y-q_x \\ q_x+q_y & q_t+q_z\end{pmatrix}$ | *Split-Quaternion Algebra* |
| $I, J, K, D$ | the images of $1, \vec e_x, \vec e_y, \vec e_z$ | this article |
| $\operatorname{Int}_P$ | conjugation by $P$, $M \mapsto PMP^{-1}$ | this article |
| $\operatorname{Aut}(\mathbb{H}_{\mathrm{s}}) \cong \mathrm{PGL}_2(\mathbb{R})$ | the automorphism group | this article |
| $\det\mathsf{M}_2(\tilde q) = \langle\tilde q\rangle_{\natural}$ | the determinant as norm | this article |
| $\operatorname{tr}\mathsf{M}_2(\tilde q) = 2\operatorname{Sc}(\tilde q)$ | the trace as twice the scalar part | this article |
| $\mathsf{M}_2(\tilde{q}^{\natural}) = \operatorname{adj}\mathsf{M}_2(\tilde q)$ | conjugation as the adjugate | this article |
| $\mathrm{SL}_2(\mathbb{R})$ | the traceless matrices, the image of $V$ | this article |
| defining module, $\mathbb{R}^2$ | the simple module of the algebra | this article |
| $R_\ell, K_\ell$ | the two families of maximal isotropic subspaces | *Split-Quaternion Zero Divisors* |
| $M_n(k)$ | matrix algebra, matrix units, Skolem–Noether | *Matrix Algebras* |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for matrix representations, matrix units and the inner automorphisms of a matrix algebra.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the Skolem–Noether theorem in its general form.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the identification $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ among the low-dimensional Clifford algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for explicit matrix models of the low-dimensional Clifford algebras.
