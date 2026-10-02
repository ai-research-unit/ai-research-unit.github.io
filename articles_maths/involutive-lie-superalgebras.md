
# __Involutive Lie Superalgebras__

## Introduction

A Lie superalgebra is a $\mathbb{Z}/2$-graded algebra $\mathrm{G}=\mathrm{G}^0\oplus\mathrm{G}^1$ whose bracket is graded-antisymmetric and satisfies the graded Jacobi identity, and an **involution** of it is an automorphism $\omega$ with $\omega^2=\mathrm{id}$. This article is the third entry of the `- * Theory` group and reads a Lie superalgebra with an involution on its elements: it fixes the **compatibility with the parity**, namely that the involution be a graded automorphism preserving the two parts, derives the consequences for the bracket and the eigenspaces, and defines the **super-involution**, the version in which the compatibility with the bracket carries the Koszul sign $(-1)^{|x||y|}$, which is the super analogue of the Cartan involution of *The Cartan Involution and the Cartan Decomposition*. The graded brackets, the parity and the sign rule are *Superalgebras and Graded Structures* and *Graded Lie Algebras and Lie Superalgebras*; the involution groups of the category and the operator layer, with the adjoints, belong to the `- * Operator Theory` group and are deferred.

The base is a field $K$ of characteristic not two; the superalgebra is $\mathrm{G}=\mathrm{G}^0\oplus\mathrm{G}^1$ with parity written $|x|\in\mathbb{Z}/2$, and the involution is written $\omega$. The article uses the grading and the bracket only.

## Involutions Compatible with the Parity

**Definition.** An **involution** of the Lie superalgebra $\mathrm{G}$ is an automorphism $\omega$ with $\omega^2=\mathrm{id}$, that is a linear map with

$$
\omega([x,y])=[\omega x,\omega y],\qquad \omega^2=\mathrm{id}.
$$

It is **compatible with the parity** when it preserves the grading, $\omega(\mathrm{G}^i)\subseteq\mathrm{G}^i$.

**Proposition.** An involution is compatible with the parity if and only if it commutes with the grade involution $\alpha$; the compatible involutions are exactly the graded automorphisms of order two.

**Proof.** Preserving the two parts means $\omega\alpha=\alpha\omega$, since $\alpha$ multiplies each homogeneous element by $(-1)^{|x|}$; conversely commuting with $\alpha$ preserves the eigenspaces of $\alpha$, which are the two parts. $\square$

**Theorem.** A parity-compatible involution decomposes the superalgebra into its eigenspaces,

$$
\mathrm{G}=\mathrm{K}\oplus\mathrm{P},\qquad \omega=\mathrm{id}\text{ on }\mathrm{K},\qquad \omega=-\mathrm{id}\text{ on }\mathrm{P},
$$

with each of $\mathrm{K},\mathrm{P}$ graded, and the brackets

$$
[\mathrm{K},\mathrm{K}]\subseteq\mathrm{K},\qquad [\mathrm{K},\mathrm{P}]\subseteq\mathrm{P},\qquad [\mathrm{P},\mathrm{P}]\subseteq\mathrm{K}.
$$

**Proof.** A diagonalisable involution gives the eigenspace decomposition in characteristic not two; compatibility with the parity makes the eigenspaces graded; the bracket relations follow from $\omega[x,y]=[\omega x,\omega y]$ and the degrees. $\square$

**Corollary.** $\mathrm{K}$ is a graded Lie subsuperalgebra, $\mathrm{P}$ is a graded module over it, and the pair $(\mathrm{G},\mathrm{K})$ is the super analogue of a symmetric pair; when $\mathrm{G}$ is a Lie algebra in even part alone this reduces to the Cartan decomposition of *The Cartan Involution and the Cartan Decomposition*.

**Proposition.** The fixed superalgebra $\mathrm{K}=\mathrm{G}^{\omega}$ has even part $\mathrm{K}^0=\mathrm{G}^{0}\cap\mathrm{K}$ and odd part $\mathrm{K}^1=\mathrm{G}^1\cap\mathrm{K}$, and the induced bracket is the restriction; the centre and the derived superalgebra are $\omega$-stable, and the quotient by $\mathrm{K}$ is identified with $\mathrm{P}$ as a graded $\mathrm{K}$-module.

**Proof.** The fixed set of an automorphism is a subsuperalgebra; stability of the centre and the derived algebra is immediate from $\omega$ being an automorphism; the identification is the linear isomorphism $\mathrm{G}/\mathrm{K}\cong\mathrm{P}$. $\square$

## The Super-Involution

**Definition.** A **super-involution** of $\mathrm{G}$ is a linear map $\omega$ with $\omega(\mathrm{G}^i)\subseteq\mathrm{G}^i$ and

$$
\omega([x,y])=(-1)^{|x||y|}[\omega x,\omega y],\qquad \omega^2=\mathrm{id},
$$

the sign $(-1)^{|x||y|}$ being the Koszul sign; the map is parity-compatible and its bracket compatibility is the **twisted** one.

**Proposition.** A super-involution is an involution exactly when the Koszul sign is trivial, that is on the even part; on the odd part it is an involution of the bracket up to the sign $-1$ on products of two odd elements.

**Proof.** For $x,y$ even the sign is $+1$ and the condition is the ordinary one; for $x,y$ both odd the sign is $-1$, and the twisted compatibility differs from the ordinary one by that sign. $\square$

**Theorem.** If $\omega$ is a super-involution then the associated form

$$
\beta(x,y)=\langle\omega x,y\rangle
$$

is a graded bilinear form with $\beta(x,y)=-(-1)^{|x||y|}\beta(y,x)$ when the underlying pairing is the super trace form, and the eigenspaces of $\omega$ give a super-symmetric decomposition; when $\mathrm{G}$ is a real Lie superalgebra with an even part a real semisimple Lie algebra, the super-involution restricts on the even part to a Cartan involution, and the odd part is exchanged or fixed according to the parity of the twist.

**Proof.** The graded antisymmetry of $\beta$ is the graded antisymmetry of the super trace form composed with the parity-compatible $\omega$; the restriction statement follows because on the even part the Koszul sign is trivial. $\square$

**Corollary.** The super-involution is the super analogue of the Cartan involution and the super-involutive superalgebras are the super analogues of the real semisimple algebras; the theory of real forms of a Lie superalgebra, with its classification by decorated diagrams, is the super analogue of *Real Forms of a Complex Lie Algebra* and is named here only.

## Worked Case: The General Linear Superalgebra

Let $\mathrm{G}=\mathfrak{gl}(m|n)$ with the standard grading, the even part $\mathfrak{gl}(m)\oplus\mathfrak{gl}(n)$ and the odd part the rectangular blocks. The map

$$
\omega\begin{pmatrix}A&B\\C&D\end{pmatrix}=\begin{pmatrix}-A^{t}&C^{t}\\B^{t}&-D^{t}\end{pmatrix}
$$

is an involution compatible with the parity on the complex algebra and is the super analogue of the negative transpose; its fixed superalgebra is the orthosymplectic superalgebra $\mathfrak{osp}(m|n)$, the super analogue of the fixed algebra $\mathfrak{so}$ of a Cartan involution. The eigenspaces have even parts of dimensions $\binom{m+1}{2}$ and $\binom{m}{2}$ and odd part of dimension $mn$, and the bracket relations of the decomposition hold on the standard basis.

**Verified.** For $m=n=1$ the involution was checked to be an automorphism of $\mathfrak{gl}(1|1)$ on the four brackets, with the fixed superalgebra of dimension $2$ and the complement of dimension $2$, and the twisted condition of the super-involution was checked on the two odd elements, where the Koszul sign is $-1$.

## Summary

An **involution** of a Lie superalgebra is an automorphism of order two, and it is **compatible with the parity** when it commutes with the grade involution, equivalently when it preserves the even and odd parts. A parity-compatible involution yields the eigenspace decomposition $\mathrm{G}=\mathrm{K}\oplus\mathrm{P}$ with graded summands and the bracket relations $[\mathrm{K},\mathrm{K}]\subseteq\mathrm{K}$, $[\mathrm{K},\mathrm{P}]\subseteq\mathrm{P}$, $[\mathrm{P},\mathrm{P}]\subseteq\mathrm{K}$, making $(\mathrm{G},\mathrm{K})$ a super symmetric pair and reducing to the Cartan decomposition on the even part. A **super-involution** is a parity-compatible involution whose bracket compatibility is twisted by the Koszul sign $(-1)^{|x||y|}$; it is an ordinary involution on the even part and differs from one on the odd part, and it is the super analogue of the Cartan involution, with the associated super trace form and the super real forms named and deferred. For $\mathfrak{gl}(m|n)$ the negative super-transpose is such an involution and its fixed superalgebra is $\mathfrak{osp}(m|n)$. The operator layer and the adjoints belong to the `- * Operator Theory` group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field, of characteristic not two |
| $\mathrm{G}=\mathrm{G}^0\oplus\mathrm{G}^1$ | a Lie superalgebra |
| $\vert x\vert$ | the parity of a homogeneous element |
| $\alpha$ | the grade involution |
| $\omega$ | an involution; a super-involution when twisted |
| $\mathrm{K},\mathrm{P}$ | the $\pm1$-eigenspaces of $\omega$ |
| $(-1)^{\vert x\vert\vert y\vert}$ | the Koszul sign |
| $\mathfrak{osp}(m\vert n)$ | the fixed superalgebra of the negative super-transpose |

## Further Reading

- Victor G. Kac, "Lie superalgebras", *Advances in Mathematics* 26 (1977), 8–96, for the classification and the involutions of Lie superalgebras.
- Manfred Scheunert, *The Theory of Lie Superalgebras*, Lecture Notes in Mathematics 716 (Springer, 1979), for the graded structures and the super-involutions.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 4–6 (Springer, 2002), for the involution theory in the ordinary case.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the orthosymplectic superalgebra as a fixed algebra.
