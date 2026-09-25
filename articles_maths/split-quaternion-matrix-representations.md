
# __Split-Quaternion Matrix Representations__

## Introduction

This article treats the split-quaternion algebra as a matrix algebra. It exhibits the faithful representation by $2 \times 2$ real matrices, proves that it exists and is unique up to conjugacy, identifies the determinant with the norm form and the trace with twice the scalar part, describes the image as a linear subspace of $M_2(\mathbb{R})$, and compares the situation with the quaternion algebra and with the eight-dimensional algebra, which admits no representation of this size.

The split-quaternion algebra, its matrix model $\Phi$ and the proof that $\Phi$ is an algebra isomorphism are assumed from *Split-Quaternion Algebra*, §*The Matrix Model*; the explicit map and its multiplicativity are not reproved here. The matrix algebra $M_n(\mathbb{R})$, its matrix units, its centre and the Skolem–Noether theorem that every automorphism of $M_n(k)$ over a field is inner are assumed from *Matrix Algebras*. The norm form and its invertibility theory are assumed from *Split-Quaternion Norm and Invertibility*; the classification of the modules of the algebra belongs to *Split-Quaternion Representations*, which cites this article for the module of the model. Nothing physical is invoked.

## The Representation

**Definition.** A **matrix representation** of $\mathbb{H}_{\mathrm{s}}$ of degree $n$ is an injective unital algebra homomorphism

$$
\Psi : \mathbb{H}_{\mathrm{s}} \longrightarrow M_n(\mathbb{R}).
$$

The representation is **faithful** by definition, since injectivity is required; its **image** is the subalgebra $\Psi(\mathbb{H}_{\mathrm{s}})$.

**Definition.** The **defining representation** of $\mathbb{H}_{\mathrm{s}}$ is the isomorphism

$$
\Phi(a + b e_1 + c e_2 + d e_3) = \begin{pmatrix} a - d & c - b \\ b + c & a + d \end{pmatrix}
$$

of (*Split-Quaternion Algebra*, §*The Matrix Model*), whose values on the generators are

$$
\Phi(1) = I, \quad \Phi(e_1) = J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \quad
\Phi(e_2) = K = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad
\Phi(e_3) = D = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}.
$$

The defining representation is the model in which every statement of this article is computed.

## Existence

**Theorem (Existence).** The split-quaternion algebra has a faithful real matrix representation of degree $2$, namely $\Phi$, and therefore

$$
\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})
$$

as real algebras.

**Proof.** By (*Split-Quaternion Algebra*, §*The Matrix Model*), the linear map $\Phi$ is an algebra homomorphism, it is injective because the four generators have linearly independent images, and it is surjective because the domain and the target both have real dimension $4$. An isomorphism is in particular an injective unital homomorphism of degree $2$. $\square$

**Corollary (Dimension).** The least degree of a faithful real matrix representation of $\mathbb{H}_{\mathrm{s}}$ is $2$. Indeed a faithful representation of degree $n$ embeds a four-dimensional algebra into $M_n(\mathbb{R})$, whose dimension is $n^2$, so $n^2 \geq 4$, and $n = 1$ is impossible because $M_1(\mathbb{R})$ is commutative while $\mathbb{H}_{\mathrm{s}}$ is not; degree $2$ is attained.

**Proof.** The inequality is the dimension count, and the non-commutativity of $\mathbb{H}_{\mathrm{s}}$ excludes $n = 1$; the defining representation attains $n = 2$. $\square$

The existence theorem is the Clifford identification of the anchor article read as a representation statement: $\mathbb{H}_{\mathrm{s}} \cong \mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ by (*The Number Systems as Clifford Algebras*).

## Uniqueness up to Conjugacy

**Theorem (Uniqueness).** Let $\Psi : \mathbb{H}_{\mathrm{s}} \to M_2(\mathbb{R})$ be a unital algebra homomorphism. Then $\Psi$ is an isomorphism, and there is an invertible matrix $P$ with

$$
\Psi(x) = P \, \Phi(x) \, P^{-1} \qquad (x \in \mathbb{H}_{\mathrm{s}}).
$$

Thus the faithful representation of degree $2$ is unique up to conjugacy: any two such representations are equivalent.

**Proof.** The kernel of $\Psi$ is a two-sided ideal of $\mathbb{H}_{\mathrm{s}}$. The algebra is simple by (*Split-Quaternion Algebra*, §*The Centre and Simplicity*), so the kernel is either $0$ or the whole algebra; it is not the whole algebra because $\Psi(1) = I \neq 0$, so it is $0$ and $\Psi$ is injective. Both sides have dimension $4$, so $\Psi$ is bijective. Now $\Psi \circ \Phi^{-1}$ is an algebra automorphism of $M_2(\mathbb{R})$, and by the Skolem–Noether theorem of *Matrix Algebras* every automorphism of $M_2(\mathbb{R})$ is inner: there is $P \in GL_2(\mathbb{R})$ with $\Psi\Phi^{-1} = \operatorname{Int}_P$. Composing with $\Phi$ gives the displayed identity. $\square$

**Corollary (The Automorphisms of the Algebra).** Every automorphism of $\mathbb{H}_{\mathrm{s}}$ is obtained by conjugating by an invertible element:

$$
\operatorname{Aut}(\mathbb{H}_{\mathrm{s}}) \cong \mathrm{PGL}_2(\mathbb{R}), \qquad \alpha(x) = g x g^{-1} \quad (g \in \mathbb{H}_{\mathrm{s}}^{\times}).
$$

**Proof.** An automorphism $\alpha$ of $\mathbb{H}_{\mathrm{s}}$ corresponds to the inner automorphism $\Phi\alpha\Phi^{-1}$ of $M_2(\mathbb{R})$, which is inner by Skolem–Noether; transport back. Conversely every inner automorphism of the algebra is an automorphism, and two units $g, g'$ give the same automorphism exactly when $g' g^{-1}$ is central, which by (*Split-Quaternion Algebra*, §*The Centre and Simplicity*) means $g' = \lambda g$ with $\lambda \in \mathbb{R}^{\times}$. $\square$

## The Determinant and the Trace

**Theorem (Determinant and Trace).** For every split-quaternion $x$,

$$
\det \Phi(x) = N(x), \qquad \operatorname{tr} \Phi(x) = 2 \operatorname{Sc}(x).
$$

The determinant of the matrix model is the norm form, a quadratic form of signature $(2,2)$, and the trace is twice the scalar part; the restriction of the trace to the vector subspace vanishes, so $\Phi(V)$ is the space of traceless matrices.

**Proof.** The determinant computation is (*Split-Quaternion Algebra*, §*The Matrix Model*) and (*Split-Quaternion Norm and Invertibility*, §*The Norm Form and the Determinant Form*). For the trace,

$$
\operatorname{tr}\Phi(a + be_1 + ce_2 + de_3) = (a - d) + (a + d) = 2a = 2\operatorname{Sc}(x).
$$

The vanishing of the trace on $V$ is the case $a = 0$. $\square$

**Corollary (Formulas in the Model).** For every $x$,

$$
\det \Phi(\bar{x}) = \det \Phi(x), \qquad \Phi(\bar{x}) = \operatorname{adj}\Phi(x),
$$

and $x$ is a unit if and only if $\Phi(x)$ is invertible, in which case $\Phi(x^{-1}) = \Phi(x)^{-1} = \operatorname{adj}\Phi(x)/\det\Phi(x)$.

**Proof.** The conjugation is an involution of the algebra, so it preserves the norm: $N(\bar{x}) = \bar{x}x = N(x)$, and the first identity follows from $\det = N$. The second is the adjugate identity of (*Split-Quaternion Algebra*, §*The Conjugation*). The invertibility statement is the equality $\det\Phi = N$ together with *Split-Quaternion Norm and Invertibility*, §*The Invertibility Criterion*. $\square$

## The Image as a Linear Subspace

**Theorem (The Image Is Everything).** The image of the defining representation is the whole matrix algebra:

$$
\Phi(\mathbb{H}_{\mathrm{s}}) = M_2(\mathbb{R}).
$$

There is no proper subalgebra of $M_2(\mathbb{R})$ of dimension $4$ other than $M_2(\mathbb{R})$ itself, so the image is not a proper linear subspace.

**Proof.** The image is a linear subspace of dimension $4$ inside the four-dimensional space $M_2(\mathbb{R})$. $\square$

The distinguished subspaces of the algebra correspond to the following subspaces of matrices.

| Subspace of $\mathbb{H}_{\mathrm{s}}$ | Image in $M_2(\mathbb{R})$ | Description |
|---|---|---|
| $S = \mathbb{R}\cdot 1$ | $\mathbb{R} I$ | the scalar matrices |
| $V = \operatorname{span}\{e_1,e_2,e_3\}$ | $\mathfrak{sl}_2(\mathbb{R})$ | the traceless matrices |
| $\mathbb{D}_2 = \operatorname{span}\{1,e_2\}$ | $\left\{\begin{pmatrix}p & q \\ q & p\end{pmatrix}\right\}$ | the symmetric matrices with equal diagonal |
| $\mathbb{D}_3 = \operatorname{span}\{1,e_3\}$ | $\left\{\begin{pmatrix}p & 0 \\ 0 & q\end{pmatrix}\right\}$ | the diagonal matrices |
| $\mathbb{H}_{\mathrm{s}} u_+$, $u_+ \mathbb{H}_{\mathrm{s}}$ | $K_{\ell_w}$, $R_{\ell_v}$ | maximal isotropic subspaces |
| $\mathbb{H}_{\mathrm{s}} u_-$, $u_- \mathbb{H}_{\mathrm{s}}$ | $K_{\ell_v}$, $R_{\ell_w}$ | maximal isotropic subspaces |

The last row is the dictionary of (*Split-Quaternion Zero Divisors*, §*The Two Families in the Algebra*), where $\ell_v$ and $\ell_w$ are the lines spanned by $(1,1)$ and $(1,-1)$ and the subspaces $R_\ell$, $K_\ell$ are the two families of maximal isotropic subspaces. The table shows that the algebra and the matrix algebra carry the same structure: the scalar part is the trace part, the vector part is the traceless part, the split-complex subalgebra $\mathbb{D}_3$ is the diagonal subalgebra, and the minimal ideals are the isotropic subspaces.

**Corollary (The Idempotents in the Model).** The idempotents of the algebra correspond to the idempotent matrices of rank one together with $0$ and $I$. In particular

$$
\Phi(u_+) = \tfrac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad
\Phi(u_-) = \tfrac12 \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix},
$$

two rank-one projections, and $\Phi(u_+) + \Phi(u_-) = I$ with $\Phi(u_+) \Phi(u_-) = 0$.

**Proof.** The images are computed from the formula for $\Phi$, and the identities are the images of the identities of (*Split-Quaternion Algebra*, §*The Idempotents*). The classification of idempotents is that of *Split-Quaternion Roots of Minus One*, §*The Relation to the Idempotents and to the Zero Divisors*. $\square$

## The Defining Module

The matrix algebra $M_2(\mathbb{R})$ acts on the column space $\mathbb{R}^2$, and through $\Phi$ this becomes an action of $\mathbb{H}_{\mathrm{s}}$.

**Definition.** The **defining module** of $\mathbb{H}_{\mathrm{s}}$ is the real vector space $\mathbb{R}^2$ with the action

$$
x \cdot v = \Phi(x) v, \qquad x \in \mathbb{H}_{\mathrm{s}}, \quad v \in \mathbb{R}^2 .
$$

**Theorem (Irreducibility).** The defining module is simple: it has no nonzero proper submodule. Consequently the defining representation is irreducible, and it is the unique irreducible representation of the algebra up to equivalence.

**Proof.** The submodules of the defining module are the $\Phi(\mathbb{H}_{\mathrm{s}})$-invariant subspaces of $\mathbb{R}^2$, and since $\Phi$ is surjective these are exactly the $M_2(\mathbb{R})$-invariant subspaces, that is, the subspaces stable under every $2 \times 2$ matrix. Let $W \neq 0$ be such a subspace and let $v = (v_1,v_2) \in W$ be nonzero. If $v_1 \neq 0$ then $E_{11}v = v_1 e_1$ lies in $W$, so $e_1 \in W$, and then $E_{12}e_1 = e_2 \in W$; if $v_1 = 0$ then $v_2 \neq 0$ and the same argument with the roles exchanged gives $e_2 \in W$ and then $e_1 \in W$. Hence $W$ contains both standard basis vectors and is the whole space. The uniqueness is the classification of the modules of a simple algebra, treated in *Split-Quaternion Representations*. $\square$

The defining module is the concrete reason the matrix model is the right one: an eight-dimensional algebra cannot be a matrix algebra of this size, but a four-dimensional simple algebra is exactly a full matrix algebra over $\mathbb{R}$, and the module of the model is the module that the algebra realises.

## Comparison with the Quaternion Case and with $\mathbb{H}_{\mathbb{D}}$

### The Quaternion Case

The quaternion algebra has no faithful real matrix representation of degree $2$.

**Proposition.** There is no injective unital algebra homomorphism $\mathbb{H} \to M_2(\mathbb{R})$.

**Proof.** Such a homomorphism would embed the four-dimensional algebra $\mathbb{H}$ into the four-dimensional algebra $M_2(\mathbb{R})$, hence would be an isomorphism, so $\mathbb{H} \cong M_2(\mathbb{R})$; but $\mathbb{H}$ is a division algebra by *Quaternion Algebra* and $M_2(\mathbb{R})$ has zero divisors. $\square$

The quaternions do have a faithful representation by $2 \times 2$ **complex** matrices, obtained from the same Pauli-type assignment with $i$ in place of the real rotation matrix: the scalar extension $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{C} = \mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$, as recorded in *The Number Systems as Clifford Algebras*, and so the quaternions act on $\mathbb{C}^2$. Over $\mathbb{R}$ the least faithful representation is of degree $4$: no representation of degree $2$ or $3$ exists, and the regular representation of the algebra on itself, of real dimension $4$, is faithful. The difference from the split case is the difference between the two real forms of the same complex algebra: the definite form gives a division algebra with no real degree-two model, the indefinite form gives the matrix algebra, which is the degree-two model itself.

**Proposition (The Least Degree over $\mathbb{R}$).** The quaternion algebra has no faithful real matrix representation of degree $2$ or $3$.

**Proof.** Degree $2$ is excluded by the preceding proposition. For degree $3$, suppose $\mathbb{H}$ acts faithfully on $\mathbb{R}^3$. Choose $v \neq 0$. The map $\mathbb{H} \to \mathbb{R}^3$, $h \mapsto hv$, is injective: if $hv = 0$ with $h \neq 0$, then multiplying by the inverse of $h$ gives $v = 0$. Hence $\mathbb{R}^3$ contains a subspace isomorphic to $\mathbb{H}$, of real dimension $4$, which is impossible. $\square$

### The Absence of a Two-Dimensional Real Model for $\mathbb{H}_{\mathbb{D}}$

The eight-dimensional algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ of the notation table has no faithful $2 \times 2$ real matrix representation, and the obstruction is dimension alone.

**Proposition.** There is no injective unital algebra homomorphism $\mathbb{H}_{\mathbb{D}} \to M_2(\mathbb{R})$.

**Proof.** Such a homomorphism would embed a real vector space of dimension $8$ into one of dimension $4$, which is impossible for an injective linear map. $\square$

The algebra is treated later in Part V, under Split-Biquaternions; nothing of it is used here beyond its dimension, which is fixed by the notation table. Its faithful linear representations have degree at least $3$, since $3^2 = 9 \geq 8$, and the description of them belongs to the later category.

## Summary

The split-quaternion algebra has a faithful real matrix representation of degree $2$, the defining representation $\Phi(a + be_1 + ce_2 + de_3) = \begin{pmatrix} a-d & c-b \\ b+c & a+d\end{pmatrix}$, and no faithful representation of lower degree. The representation is unique up to conjugacy: every unital algebra homomorphism $\mathbb{H}_{\mathrm{s}} \to M_2(\mathbb{R})$ is an isomorphism, and any two differ by conjugation by an invertible matrix. The automorphism group of the algebra is $\mathrm{PGL}_2(\mathbb{R})$, acting by inner automorphisms.

The determinant of the model is the norm form $N$, of signature $(2,2)$, and the trace is twice the scalar part; the vector subspace is the traceless part, and conjugation is the adjugate. The image of the algebra is the whole of $M_2(\mathbb{R})$, and the distinguished subspaces of the algebra correspond to the scalar matrices, the traceless matrices, the diagonal subalgebra, the symmetric subalgebra, the minimal ideals and the two families of maximal isotropic subspaces. The defining module $\mathbb{R}^2$ is simple, and it is the unique irreducible module of the algebra.

The quaternion algebra has no faithful real degree-two representation, because an isomorphism with $M_2(\mathbb{R})$ would contradict its being a division algebra, although its complexification is $M_2(\mathbb{C})$; the eight-dimensional algebra has none either, by the dimension count alone, and its representations belong to the later category.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\Psi$ | a matrix representation of $\mathbb{H}_{\mathrm{s}}$ | this article |
| $\Phi$ | the defining representation, $x \mapsto \begin{pmatrix} a-d & c-b \\ b+c & a+d\end{pmatrix}$ | *Split-Quaternion Algebra* |
| $I, J, K, D$ | the images of $1, e_1, e_2, e_3$ | this article |
| $\operatorname{Int}_P$ | conjugation by $P$, $M \mapsto PMP^{-1}$ | this article |
| $\operatorname{Aut}(\mathbb{H}_{\mathrm{s}}) \cong \mathrm{PGL}_2(\mathbb{R})$ | the automorphism group | this article |
| $\det\Phi(x) = N(x)$ | the determinant as norm form | this article |
| $\operatorname{tr}\Phi(x) = 2\operatorname{Sc}(x)$ | the trace as twice the scalar part | this article |
| $\Phi(\bar{x}) = \operatorname{adj}\Phi(x)$ | conjugation as the adjugate | this article |
| $\mathfrak{sl}_2(\mathbb{R})$ | the traceless matrices, the image of $V$ | this article |
| defining module, $\mathbb{R}^2$ | the simple module of the algebra | this article |
| $R_\ell, K_\ell$ | the two families of maximal isotropic subspaces | *Split-Quaternion Zero Divisors* |
| $M_n(k)$ | matrix algebra, matrix units, Skolem–Noether | *Matrix Algebras* |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for matrix representations, matrix units and the inner automorphisms of a matrix algebra.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the Skolem–Noether theorem in its general form.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the identification $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ among the low-dimensional Clifford algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for explicit matrix models of the low-dimensional Clifford algebras.
