
# __Hermitian Forms over a Local Field__

## Introduction

A local field is a field complete with respect to a nontrivial absolute value and locally compact: the real numbers, the complex numbers, a finite extension of the $p$-adic numbers $\mathbb{Q}_p$, or the field of formal Laurent series over a finite field. A Hermitian form over such a field is a sesquilinear form that is equal to its own conjugate transpose, and the problem of the theory is the classification: when are two of them isometric? Over the real and complex fields the answer is the signature; over a non-Archimedean local field it is the rank together with the discriminant and the Hasse invariant. This article states the definitions, the classification, the role of the norm form of a quadratic extension, and the local duality that makes the invariants complete. It is the entry point of the Hermitian-forms part of the category; the global positivity is *Positivity and the Explicit Formula* and *Hermitian Forms and the Zeta Function*, and the non-Archimedean analytic side is *Involutions of a Rigid Analytic Space*.

The conventions are those fixed for the category. $K$ is a local field, $c$ is an involution of $K$ (the identity or the conjugation of a quadratic extension), and the fixed field of $c$ is $K_0$. A **Hermitian form** on $K^n$ is a form $h(x,y)$ with $h(x,y)=c(h(y,x))$ and $h$ linear in the first variable, represented by a matrix $H$ with $H^*=H$, where $H^*=\overline{H}^{\mathsf T}$ and the bar is $c$ applied entrywise. Nothing here reads a distance as an object.

## Local Fields and Involutions

### The local fields

**Theorem.** The local fields are $\mathbb{R}$, $\mathbb{C}$, the finite extensions of $\mathbb{Q}_p$, and the finite extensions of $\mathbb{F}_p((t))$. Each is complete, locally compact, and has a unique maximal compact subring when it is non-Archimedean. The involutions of a local field are the identity, and, when $K$ is a quadratic extension of $K_0$, the nontrivial element of the Galois group.

**Proof.** This is the classification of the locally compact fields, in *Local Fields*; the statement about the involutions is the fundamental theorem of Galois theory for the quadratic extension together with the fact that $\mathbb{R}$ and $\mathbb{C}$ admit only the identity and complex conjugation.

### Hermitian and symmetric forms

**Definition.** Let $(K,c)$ be a local field with involution. A form $h$ is **Hermitian** if $h(x,y)=c(h(y,x))$, and **symmetric** if $c=\mathrm{id}$ and $h(x,y)=h(y,x)$. A Hermitian form over a non-Archimedean $(K,c)$ is **nondegenerate** if its matrix $H$ is invertible.

**Proposition.** The isometry group of a nondegenerate Hermitian form is the unitary group $U(H)=\{g:g^*Hg=H\}$, a closed subgroup of $\mathrm{GL}_n(K)$, compact modulo the scalars when $K$ is non-Archimedean. The forms on $K^n$ correspond to the $c$-Hermitian matrices, and the isometry classes correspond to the orbits of $\mathrm{GL}_n(K)$ acting by $H\mapsto g^*Hg$.

**Proof.** This is the definition of the isometry group and the change-of-basis formula for the matrix of a form; the compactness statement is the standard property of the unitary groups over a non-Archimedean field, in *Local Fields*.

## Classification

### Archimedean

**Theorem.** Over $\mathbb{R}$ with $c=\mathrm{id}$ the nondegenerate symmetric forms are classified by the signature $(p,q)$, $p+q=n$; over $\mathbb{C}$ with $c=\mathrm{id}$ the nondegenerate forms are classified by the rank $n$; over $\mathbb{C}$ with $c$ the complex conjugation the nondegenerate Hermitian forms are classified by the signature $(p,q)$.

**Proof.** Sylvester's law of inertia for the real case; for the complex bilinear case the Gram–Schmidt argument over $\mathbb{C}$ diagonalises the form to $x_1^2+\dots+x_n^2$ with the coefficients absorbed by a square root; for the complex Hermitian case the spectral theorem for Hermitian matrices, in *Spectral Theory*.

### Non-Archimedean

**Definition.** For a nondegenerate Hermitian form $H$ over a non-Archimedean $(K,c)$ the **discriminant** is $\operatorname{disc}(H)=\det(H)\in K_0^\times/N(K^\times)$, where $N$ is the norm of the extension when $c\ne\mathrm{id}$ and $K_0=K$ when $c=\mathrm{id}$; the **Hasse invariant** is $s(H)\in\{\pm1\}$.

**Theorem (local classification).** Over a non-Archimedean local field with involution, two nondegenerate Hermitian forms are isometric if and only if they have the same rank, the same discriminant and the same Hasse invariant. The invariants are complete, and every compatible triple of rank, discriminant and Hasse invariant is realised by a form.

**Proof.** The proof is the Witt cancellation theorem applied to the decomposition of the form into orthogonal hyperbolic planes and an anisotropic residual form of rank at most two; the residual form is determined by its discriminant and its Hasse invariant, and the hyperbolic planes are unique up to isometry. This is the local theory of *Quadratic Forms* and *Hermitian Forms over a Local Field*.

### The norm form

**Theorem.** Let $L/K$ be a quadratic extension with conjugation $c$ and norm $N$. The Hermitian form $h(x,y)=\sum_i x_i\,c(y_i)$ on $L^n$, whose diagonal entries are $1$ and which is the **norm form** $\sum_iN(x_i)$, has discriminant $1$ and its Hasse invariant is the **Hasse invariant of the extension**, an element of $\{\pm1\}$ equal to the class of the extension in $K_0^\times/N(L^\times)$; the two are related by the local reciprocity law.

**Proof.** The norm form is diagonal with entries $1$; its determinant is $1$ and its discriminant is trivial; the computation of the Hasse invariant is the Hilbert symbol of the extension, and the local reciprocity law identifies the symbol with the norm class. This is the local class field theory of *Local Fields*.

## Local Duality

**Theorem.** Let $(K,c)$ be non-Archimedean with residue characteristic not $2$, and let $H$ be a nondegenerate Hermitian form of rank $n$. The bilinear form on $K^n$ associated with $H$ is nondegenerate and defines a duality $K^n\times K^n\to K$; the dual of a lattice is a lattice, and the invariants of the form are the invariants of the duality. In particular the discriminant controls the self-dual lattices and the Hasse invariant controls the existence of an isotropic vector.

**Proof.** The matrix $H$ is invertible, so the form is a perfect pairing; the lattice statements are elementary once the pairing is perfect, and the existence of an isotropic vector over a non-Archimedean local field is decided by the Hasse invariant because the anisotropic residual form has rank at most two. This is the standard local duality of *Quadratic Forms*.

## Worked Examples

**Example ($K=\mathbb{R}$).** The standard form $x_1^2+\dots+x_p^2-x_{p+1}^2-\dots-x_n^2$ has signature $(p,n-p)$; the isometry group is $O(p,n-p)$.

**Example ($K=\mathbb{C}$, $c$ the conjugation).** The form $\sum|x_i|^2$ has signature $(n,0)$ and isometry group the unitary group $U(n)$; the form $\sum_{i\le p}|x_i|^2-\sum_{i>p}|x_i|^2$ has signature $(p,n-p)$.

**Example ($K=\mathbb{Q}_p$, $c=\mathrm{id}$).** The forms $\langle1,1,\dots,1\rangle$ of rank $n$ have discriminant $1$ and Hasse invariants varying with $n$ and $p$; the form $\langle1,-1\rangle$ is hyperbolic and represents zero.

**Example (the norm form of $\mathbb{Q}_p(\sqrt{p})$).** The extension is ramified, the norm form has Hasse invariant $-1$, and it is anisotropic of rank $2$; this is the boundary between the hyperbolic and the anisotropic cases.

## Failure of the Degenerate Cases

The classification fails in four degenerate configurations. First, in residue characteristic $2$ the discriminant and the Hasse invariant are not complete invariants; the Arf invariant or the quadratic refinement is needed, and the Witt group is more complicated. Second, when the involution $c$ is trivial over a field of characteristic $2$ the symmetric forms are not Hermitian forms in the sense of the article, and the classification must be redone for the quadratic forms. Third, a degenerate form, with $\det H=0$, has a radical and the isometry problem is the isometry problem of a form on the quotient by the radical plus the position of the radical; the invariants of the nondegenerate part do not determine the form. Fourth, over $\mathbb{C}$ with the trivial involution the signature is not an invariant and the classification is by rank alone; this is the degenerate case where one of the two non-Archimedean invariants disappears. These are the boundary cases of the local theory.

## Summary

Over a local field with involution, a Hermitian form is a sesquilinear form equal to its conjugate transpose, and its isometry class is classified by the signature in the Archimedean case and by the rank, the discriminant and the Hasse invariant in the non-Archimedean case. The norm form of a quadratic extension is the diagonal Hermitian form $\sum N(x_i)$, whose Hasse invariant is the local reciprocity symbol of the extension. The local duality, which is the perfect pairing defined by a nondegenerate form, makes the invariants complete and decides the existence of isotropic vectors over a non-Archimedean field. The degenerate cases are the residue characteristic $2$, the trivial involution in characteristic $2$, the degenerate forms with a radical and the complex case with the trivial involution.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(K,c)$ | Local field with involution |
| $K_0$ | Fixed field of $c$ |
| $h(x,y)=c(h(y,x))$ | Hermitian form |
| $H^*=H$, $H^*=\overline{H}^{\mathsf T}$ | Matrix condition |
| $(p,q)$ | Signature (Archimedean) |
| $\operatorname{disc}(H)=\det H\in K_0^\times/N(K^\times)$ | Discriminant |
| $s(H)\in\{\pm1\}$ | Hasse invariant |
| $N$ | Norm of a quadratic extension |
| $U(H)$ | Isometry group |

## Further Reading

- John Cassels and Albrecht Fröhlich, *Algebraic Number Theory* (Academic Press, 1967), for the local fields and the local reciprocity.
- Tsit Yuen Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the Witt group and the classification.
- Martin Eichler, *Quadratic Forms and Orthogonal Groups* (Birkhäuser, 1957), for the Hermitian classification.
- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for the local fields, the norms and the reciprocity.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the general classification theorems.
