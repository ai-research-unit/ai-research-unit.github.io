# __Symmetric Pairs and Cartan Pairs: the Reductivity Criterion at $n=2$__

## Introduction

**A symmetric pair is an involution of a Lie algebra together with its two eigenspaces, the criterion of reductivity asks for an invariant complement, and at order two every pair of $\mathfrak{sl}_2$ passes the criterion while the nilpotent direction of the triangular algebra shows how it fails.**

The article defines symmetric pairs and Cartan pairs, proves the structure equations $[\mathfrak{h},\mathfrak{h}]\subseteq\mathfrak{h}$, $[\mathfrak{h},\mathfrak{p}]\subseteq\mathfrak{p}$, $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{h}$, proves the reductivity criterion and shows that semisimple algebras satisfy it with $\mathfrak{p}=\mathfrak{h}^{\perp}$ for the Killing form. At order two it lists the two pairs of $\mathfrak{sl}_2(\mathbb{R})$ with their Killing forms, identifies the Cartan pair, and exhibits the degenerate trace form on the triangular algebra where the criterion has no input. It assumes *The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_2(\mathbb{C})$* and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$*.

It defers the four forms and their norms to *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, where the same two halves carry the corresponding real forms.

## Symmetric Pairs

**Definition.** A **symmetric pair** $(\mathfrak{g},\mathfrak{h},\mathfrak{p})$ is a Lie algebra $\mathfrak{g}$ with an involutive automorphism $\sigma$, a subalgebra $\mathfrak{h}=\{X:\sigma X=X\}$, and the space $\mathfrak{p}=\{X:\sigma X=-X\}$.

**Proposition.** The two eigenspaces satisfy

$$
\mathfrak{g}=\mathfrak{h}\oplus\mathfrak{p},\qquad [\mathfrak{h},\mathfrak{h}]\subseteq\mathfrak{h},\qquad [\mathfrak{h},\mathfrak{p}]\subseteq\mathfrak{p},\qquad [\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{h}.
$$

**Proof.** Every $X$ is $\tfrac12(X+\sigma X)+\tfrac12(X-\sigma X)$, and the two terms lie in the two eigenspaces; the sum is direct because an element in both is zero. For the brackets, apply $\sigma$ to $[X,Y]$ and use that $\sigma$ is an automorphism: $\sigma[X,Y]=[\sigma X,\sigma Y]$, and the signs multiply.

**Definition.** A **Cartan pair** is a symmetric pair together with a symmetric pair $(\mathfrak{g},\mathfrak{k},\mathfrak{p})$ whose $\mathfrak{k}$ is the fixed algebra of a Cartan involution; the involution is then required to make the form $\langle X,\sigma Y\rangle$ positive definite.

**The two notions differ.** Every Cartan pair is a symmetric pair, and a symmetric pair is Cartan exactly when the fixed algebra is the compact one.

## The Reduction to Two Pieces

**Proposition.** The pair is determined by $\mathfrak{h}$ and $\mathfrak{p}$, and the Jacobi identity is equivalent to the three conditions: $\mathfrak{p}$ is an $\mathfrak{h}$-module and the bracket on $\mathfrak{p}$ is $\mathfrak{h}$-equivariant.

**Proof.** The three inclusions of the previous section are the content of the Jacobi identity applied to the signs of the three elements; the module statement is the middle inclusion.

**Proposition.** For $X,Y\in\mathfrak{p}$ the operator $\operatorname{ad}X$ maps $\mathfrak{h}$ to $\mathfrak{p}$ and $\mathfrak{p}$ to $\mathfrak{h}$, so in the splitting of the space it is off-diagonal.

**Proof.** The bracket of $\mathfrak{p}$ with $\mathfrak{h}$ lands in $\mathfrak{p}$ and the bracket of $\mathfrak{p}$ with itself lands in $\mathfrak{h}$.

**The pair is the same object as a grading.** The map $\sigma$ gives the algebra a grading by $\mathbb{Z}/2$, with $\mathfrak{h}$ in degree $0$ and $\mathfrak{p}$ in degree $1$; the structure equations are the statement that the grading is compatible with the bracket.

## The Reductivity Criterion

**Definition.** The pair is **reductive** when there is a subspace $\mathfrak{q}$ with $\mathfrak{g}=\mathfrak{h}\oplus\mathfrak{q}$ and $[\mathfrak{h},\mathfrak{q}]\subseteq\mathfrak{q}$.

**Proposition (the criterion).** The pair is reductive as soon as $\mathfrak{h}$ is reductive and $\mathfrak{p}$ is completely reducible as an $\mathfrak{h}$-module; and it fails to be reductive as soon as $\mathfrak{p}$ contains an invariant subspace with no invariant complement.

**Proof.** Complete reducibility writes $\mathfrak{p}$ as a sum of invariant subspaces, and together with $\mathfrak{h}$ they give an invariant decomposition of $\mathfrak{g}$, so the pair is reductive. For the second statement, an invariant complement to the invariant subspace would be an invariant complement inside $\mathfrak{p}$, which does not exist.

**The criterion is a statement about the module, not about the algebra.** What can fail is the existence of an invariant complement; the bracket itself always satisfies the three structure equations.

**Corollary.** If $\mathfrak{h}$ is abelian and $\mathfrak{p}$ splits as a sum of one-dimensional $\mathfrak{h}$-modules, the pair is reductive.

**Proof.** A one-dimensional module is irreducible, so the sum of such modules is completely reducible, and an abelian algebra is reductive by definition.

## Why Semisimple Algebras Pass

**Theorem.** Let $\mathfrak{g}$ be semisimple with Killing form $\langle,\rangle$, and let $\sigma$ be an automorphism with $\sigma^{2}=\mathrm{id}$. Then $\mathfrak{p}=\mathfrak{h}^{\perp}$, so the pair is reductive.

**Proof.** Automorphisms preserve the Killing form: $\langle\sigma X,\sigma Y\rangle=\langle X,Y\rangle$. Hence $\langle\sigma X,Y\rangle=\langle X,\sigma Y\rangle$, so $\sigma$ is self-adjoint and the eigenspaces are orthogonal by the criterion of *The Two Halves as Orthogonal Complements at $n=2$*. Since $\mathfrak{p}$ is the orthogonal complement of $\mathfrak{h}$ and the form is nondegenerate, $\mathfrak{p}$ is an $\mathfrak{h}$-invariant complement.

**Corollary.** Every symmetric pair of a semisimple Lie algebra is reductive, and the decomposition $\mathfrak{g}=\mathfrak{h}\oplus\mathfrak{p}$ is orthogonal for the Killing form.

**Proof.** The theorem gives the invariance and the orthogonality at once.

**The trace form works the same way on a semisimple algebra of matrices.** For $\mathfrak{g}=\mathfrak{sl}_2(\mathbb{R})$ the trace form is a nonzero multiple of the Killing form, so the same argument applies with either form.

## The Two Symmetric Pairs of $\mathfrak{sl}_2(\mathbb{R})$

**The first pair.** Let $\sigma(A)=A^{\mathsf T}$ on $\mathfrak{sl}_2(\mathbb{R})$. Then $\mathfrak{h}=\mathfrak{so}(2)=\mathbb{R}J$ and $\mathfrak{p}$ is the space of traceless symmetric matrices, of dimension $2$.

**Proof.** The transpose is an involutive automorphism of $\mathfrak{sl}_2(\mathbb{R})$, its fixed space is the antisymmetric traceless matrices, and the traceless symmetric matrices form the other eigenspace.

**The structure equations hold.** $[\mathfrak{so}(2),\mathfrak{p}]\subseteq\mathfrak{p}$ and $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{so}(2)$, the second because the bracket of two symmetric matrices is antisymmetric.

**Proof.** $[J,S]=JS-SJ$ is symmetric for symmetric $S$ and has trace zero; $[S_{1},S_{2}]$ is antisymmetric for symmetric $S_{i}$. Numerically, with $S_{1}=\begin{pmatrix}1&2\\ 2&-1\end{pmatrix}$ and $S_{2}=\begin{pmatrix}0&1\\ 1&3\end{pmatrix}$, the bracket is $8J$.

**The second pair.** Let $\sigma(A)=DAD^{-1}$ with $D=\operatorname{diag}(1,-1)$. Then $\mathfrak{h}=\mathbb{R}(E_{11}-E_{22})$ and $\mathfrak{p}=n_+\oplus n_-$.

**Proof.** Conjugation by $D$ preserves the diagonal and multiplies $E_{12}$ and $E_{21}$ by $-1$; it is an involutive automorphism, and $\mathfrak{sl}_2(\mathbb{R})$ is spanned by the three lines.

**The structure equations hold.** $[H,E_{12}]=2E_{12}$ and $[H,E_{21}]=-2E_{21}$, so each root line is stable; $[E_{12},E_{21}]=H$ lands in $\mathfrak{h}$.

**Corollary.** Both pairs are reductive, and they are not conjugate: the first has a one-dimensional compact fixed algebra and the second does not.

**Proof.** Reductivity is the theorem for semisimple algebras; $\mathfrak{so}(2)$ is compact since the Killing form is negative definite on it, and $\mathbb{R}H$ is not compact since the Killing form is positive on $H$.

**The Killing form separates them.** In the basis $H,E_{12},E_{21}$ the matrix of the Killing form is $\operatorname{diag}(8)\oplus\begin{pmatrix}0&4\\ 4&0\end{pmatrix}$, whose eigenvalues are $-4,4,8$.

**Proof.** The brackets of the three basis elements in themselves are the structure constants of $\mathfrak{sl}_2$, and the trace of the product of the two adjoint matrices gives the displayed entries; the eigenvalues are computed from the characteristic polynomial.

## The Cartan Pair

**Definition.** The pair $(\mathfrak{sl}_2(\mathbb{R}),\mathfrak{so}(2),\mathfrak{p})$ with $\sigma(A)=A^{\mathsf T}$ is the Cartan pair of $\mathfrak{sl}_2(\mathbb{R})$.

**Proposition.** The form $\langle X,Y\rangle_{\sigma}=\langle X,\sigma Y\rangle$ built from the Killing form is positive definite, so $\sigma$ is a Cartan involution.

**Proof.** On $\mathfrak{h}=\mathfrak{so}(2)$ the form is $-\langle X,X\rangle$, which is positive because the Killing form is negative definite on the compact line; on $\mathfrak{p}$ the form is $\langle X,X\rangle$, which is positive because the form is positive definite on the two-dimensional space of traceless symmetric matrices; the two spaces are orthogonal.

**Corollary.** $\mathfrak{sl}_2(\mathbb{R})=\mathfrak{so}(2)\oplus\mathfrak{p}$ is a Cartan decomposition, and $\mathrm{SO}(2)$ is a maximal compact subgroup of $\mathrm{SL}_2(\mathbb{R})$.

**Proof.** The decomposition is orthogonal for the positive definite form, and the global statement is the theorem that the fixed group of a Cartan involution is maximal compact.

**The inertia of the two pairs is the same and the packaging differs.** Both pairs have $\dim\mathfrak{h}=1$ and $\dim\mathfrak{p}=2$; in the Cartan pair the fixed line is the one on which the form is negative, and in the second pair the fixed line is the one on which the form is positive.

## Where the Criterion Fails at $n=2$

**The hypothesis that fails is the nondegeneracy of the form.** The criterion is applied through the Killing form or the trace form; on a subalgebra where that form is degenerate, the orthogonal complement is larger than the complementary dimension and the argument gives nothing.

**Proposition.** On the two-dimensional subalgebra spanned by $H=E_{11}-E_{22}$ and $E_{12}$ the trace form has matrix $\begin{pmatrix}2&0\\ 0&0\end{pmatrix}$, of rank one, with radical $\mathbb{R}E_{12}$.

**Proof.** $\operatorname{tr}(H^{2})=2$, $\operatorname{tr}(HE_{12})=0$ and $\operatorname{tr}(E_{12}^{2})=0$.

**Corollary.** The line $\mathbb{R}E_{12}$ is an ideal of that subalgebra and lies in the radical of the form, so no complement of the ideal can be found from the form.

**Proof.** $[H,E_{12}]=2E_{12}$ shows that the line is an ideal; the radical contains it by the computation above, so the form vanishes on the quotient direction.

**The lesson at order two.** Reductivity is a property of semisimple algebras and of their symmetric pairs; it fails first at the nilpotent directions, which are exactly the directions that the trace form cannot see.

## Summary

A symmetric pair is an involutive automorphism of a Lie algebra with its two eigenspaces $\mathfrak{h}$ and $\mathfrak{p}$, satisfying $[\mathfrak{h},\mathfrak{h}]\subseteq\mathfrak{h}$, $[\mathfrak{h},\mathfrak{p}]\subseteq\mathfrak{p}$ and $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{h}$. The pair is reductive when an $\mathfrak{h}$-invariant complement exists, and for a semisimple algebra the Killing form supplies one, namely $\mathfrak{p}=\mathfrak{h}^{\perp}$.

At order two $\mathfrak{sl}_2(\mathbb{R})$ has two symmetric pairs: the transpose with fixed algebra $\mathfrak{so}(2)$, which is the Cartan pair, and the conjugation by $\operatorname{diag}(1,-1)$ with fixed algebra the split Cartan, which is not Cartan. The Killing form has matrix $\operatorname{diag}(8)\oplus\begin{pmatrix}0&4\\4&0\end{pmatrix}$ in the basis $H,E_{12},E_{21}$, with eigenvalues $-4,4,8$. On the triangular subalgebra the trace form is degenerate with radical the nilpotent line, and that is where the criterion loses its input.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$ | the involutive automorphism of the pair |
| $\mathfrak{h}$ | the fixed algebra, the $+1$ eigenspace |
| $\mathfrak{p}$ | the other eigenspace, the $-1$ eigenspace |
| $\mathfrak{q}$ | an $\mathfrak{h}$-invariant complement |
| $\mathfrak{so}(2)$ | $\mathbb{R}J$, the compact fixed algebra |
| $\mathbb{R}H$ | the split Cartan, the noncompact fixed line |
| $\langle,\rangle$ | the Killing form |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for symmetric pairs, Cartan involutions and the reductivity criterion.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2002), for the classification of the symmetric pairs of the classical algebras.
- [The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_2(\mathbb{C})$](the-triangular-decomposition-h-n-plus-n-minus-of-m2c.html), for the bracket data used on both pairs.
- [The Two Halves as Orthogonal Complements at $n=2$](the-two-halves-as-orthogonal-complements-at-n-2.html), for the symmetry that makes $\mathfrak{p}$ the orthogonal complement.
- [The Involutions of $M_2(\mathbb{C})$ over $\mathbb{R}$ and over $\mathbb{C}$](the-involutions-of-m2c-over-r-and-over-c.html), for the full list of involutions from which the pairs are built.
