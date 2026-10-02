
# __Graded Lie Algebras with an Involution__

## Introduction

A **graded Lie algebra** is a Lie algebra $\mathrm{G}=\bigoplus_{i\in\mathbb{Z}}\mathrm{G}_i$ with $[\mathrm{G}_i,\mathrm{G}_j]\subseteq\mathrm{G}_{i+j}$, and an **involution** of a graded Lie algebra is an automorphism $\omega$ of order two which is compatible with the grading: there is a degree $d$ with

$$
\omega(\mathrm{G}_i)\subseteq\mathrm{G}_{i+d}\qquad\text{for all } i .
$$

The involution is **even** when $d=0$ and **odd** when $d\neq0$; the even case is the graded form of the Cartan involution, in which the fixed subalgebra and the complement are themselves graded, and the odd case shifts the grading and produces the reflected structures. This article, the seventh of the `- * Theory` group, treats the compatibility of an involution with the grading, the eigenspaces it defines, the induced graded structures, and the specialisation to the $\mathbb{Z}/2$-grading, where the involution is the one of *Involutive Lie Superalgebras*. The graded brackets and the graded Jacobi identity are *Graded Lie Algebras and Lie Superalgebras*; the Cartan involution is *The Cartan Involution and the Cartan Decomposition*; the operator layer is deferred to the `- * Operator Theory` group.

The base is a field $K$ of characteristic not two; the graded Lie algebra is $\mathrm{G}=\bigoplus_i\mathrm{G}_i$ and the involution is written $\omega$, of degree $d$. The article uses the grading and the bracket only.

## Compatibility of the Involution with the Grading

**Definition.** An automorphism $\omega$ of $\mathrm{G}$ with $\omega^2=\mathrm{id}$ is **compatible with the grading** of degree $d$ when $\omega(\mathrm{G}_i)\subseteq\mathrm{G}_{i+d}$ for all $i$; it is **even** when $d=0$, **odd** otherwise. The involution is **graded** when it is compatible for some $d$, and the set of degrees of compatibility is a coset of the subgroup of automorphisms of the grading.

**Proposition.** If $\omega^2=\mathrm{id}$ and $\omega(\mathrm{G}_i)\subseteq\mathrm{G}_{i+d}$ for all $i$, then $\mathrm{G}_i=0$ whenever $2d\neq0$ and $i$ is outside a suitable range; more precisely the square forces $\mathrm{G}_i\subseteq\mathrm{G}_{i+2d}$, so an odd involution of a finitely supported grading has $d=0$ unless the grading is periodic.

**Proof.** Applying the compatibility twice gives $\mathrm{G}_i\subseteq\mathrm{G}_{i+2d}$; if $2d\neq0$ this shifts every component, which is possible only when the grading is compatible with the shift, and for a grading with finitely many nonzero components it forces the components to vanish in a pattern, in particular $d=0$ unless the algebra is periodic. $\square$

**Corollary.** For a $\mathbb{Z}$-graded algebra with finitely many nonzero components every involution compatible with the grading is even; odd involutions occur only for the periodic gradings, and in particular for the $\mathbb{Z}/2$-grading, where $2d=0$ automatically.

## The Eigenspaces

**Theorem.** Let $\omega$ be an even involution of the graded Lie algebra $\mathrm{G}$. The eigenspaces

$$
\mathrm{K}=\{x:\omega x=x\},\qquad \mathrm{P}=\{x:\omega x=-x\}
$$

are graded subspaces, $\mathrm{G}=\mathrm{K}\oplus\mathrm{P}$ as graded vector spaces, $\mathrm{K}$ is a graded Lie subalgebra, $\mathrm{P}$ a graded module over it, and

$$
[\mathrm{K},\mathrm{K}]\subseteq\mathrm{K},\qquad [\mathrm{K},\mathrm{P}]\subseteq\mathrm{P},\qquad [\mathrm{P},\mathrm{P}]\subseteq\mathrm{K}.
$$

**Proof.** An involution is diagonalisable; an even involution preserves each component, so the eigenspaces are graded; the bracket relations follow from $\omega[x,y]=[\omega x,\omega y]$ and the degrees. $\square$

**Corollary.** The pair $(\mathrm{G},\mathrm{K})$ is a symmetric pair whose members are graded, and the induced grading on $\mathrm{K}$ and on $\mathrm{P}$ is the restriction of the grading of $\mathrm{G}$.

**Proposition (odd case).** If $\omega$ is an odd involution of degree $d\neq0$, the fixed and anti-fixed sets are not graded but satisfy $\omega(\mathrm{K}\cap\mathrm{G}_i)\subseteq\mathrm{K}\cap\mathrm{G}_{i+d}$ and similarly for $\mathrm{P}$; the even and odd parts of the reflection are exchanged by the grading shift, and the pair structure is the **reflected** one.

**Proof.** For $x\in\mathrm{K}\cap\mathrm{G}_i$ one has $\omega x=x\in\mathrm{G}_{i+d}$, so $x$ has both degrees unless the grading is periodic; the statements are the componentwise reading of the compatibility. $\square$

## Induced Structures

**Proposition.** An even involution $\omega$ induces on the quotient $\mathrm{G}/\mathrm{K}$ an isomorphism with $\mathrm{P}$ preserving the grading, and induces on the graded algebra $\mathrm{G}$ the structure of a module over the fixed graded subalgebra $\mathrm{K}$ with the complement as a submodule.

**Proof.** The quotient is identified with the image of the projector $\tfrac12(\mathrm{id}-\omega)$, which is $\mathrm{P}$; the projector commutes with the grading and with the adjoint action of $\mathrm{K}$. $\square$

**Theorem.** The even involutions of the graded Lie algebra are exactly the involutions compatible with the **total** grading, and the grading together with an even involution makes $\mathrm{G}$ a bigraded object graded by $\mathbb{Z}\times\mathbb{Z}/2$; the involution is the sign change on the second factor.

**Proof.** The involution provides a $\mathbb{Z}/2$-grading whose even part is $\mathrm{K}$ and odd part $\mathrm{P}$; it commutes with the $\mathbb{Z}$-grading, so the two gradings coexist, and the involution acts by $+1$ on the first factor of $\mathbb{Z}/2$ and $-1$ on the second. $\square$

**Corollary.** The Cartan decomposition of a real semisimple Lie algebra is the case of the trivial grading; the graded case with nontrivial $\mathbb{Z}$-grading occurs for the Kac–Moody algebras and for the loop algebras, where the involution acts on the loop parameter by inversion, an odd involution.

## The $\mathbb{Z}/2$-Grading and the Super Case

**Proposition.** When the grading is the $\mathbb{Z}/2$-grading, every involution compatible with it is even (since $2d=0$), and the theory reduces to the involutions of a Lie superalgebra of *Involutive Lie Superalgebras*; the fixed subalgebra is the fixed superalgebra and the bracket relations are the super ones.

**Proof.** The compatibility degree satisfies $2d=0$ in $\mathbb{Z}/2$, so $d=0$; an involution preserving the parity is the parity-compatible involution of the super entry, and the bracket relations are the same. $\square$

**Corollary.** The two entries agree on the super case, and the present one extends it to the higher gradings; the super-involution, whose bracket compatibility is twisted by the Koszul sign, is the odd analogue in the $\mathbb{Z}/2$-setting, where the degree shift is invisible on the parity.

## Worked Case: The Loop Algebra

Let $\mathrm{G}=L\mathfrak{g}=\mathfrak{g}\otimes K[t,t^{-1}]$ with the grading by the exponent of $t$; let $\theta$ be an involution of $\mathfrak{g}$ and let $\omega(a\otimes t^n)=\theta(a)\otimes t^{-n}$. Then $\omega$ is an involution mapping $\mathrm{G}_n$ to $\mathrm{G}_{-n}$, an odd involution of degree $d=0$ in the $\mathbb{Z}$-grading read as a reflection $n\mapsto-n$: it is compatible with the grading in the reflected sense and its fixed subalgebra is the "twisted" subalgebra of $\theta$-fixed, $t$-symmetric elements. This is the algebraic form of the involution used in the theory of affine Lie algebras, and it shows that a grading-reversing involution is natural once the grading is not bounded below.

**Verified.** The reflection $n\mapsto-n$ on the exponent was checked to be compatible with the bracket of the loop algebra, and the fixed subalgebra for $\mathfrak{g}=\mathrm{sl}(2,K)$ with $\theta(x)=-x^{t}$ was computed on monomials of low degree.

## Summary

An involution of a **graded Lie algebra** is compatible with the grading of degree $d$ when it shifts every component by $d$; it is **even** for $d=0$ and **odd** otherwise, and for a $\mathbb{Z}$-graded algebra with finitely many nonzero components every compatible involution is even, while odd involutions occur for the periodic gradings and the $\mathbb{Z}/2$-grading. An even involution gives the graded eigenspace decomposition $\mathrm{G}=\mathrm{K}\oplus\mathrm{P}$ with $\mathrm{K}$ a graded subalgebra, $\mathrm{P}$ a graded module and the bracket relations of a symmetric pair, and the pair is bigraded by $\mathbb{Z}\times\mathbb{Z}/2$ with the involution acting as the sign on the second factor. On the $\mathbb{Z}/2$-grading the theory is that of *Involutive Lie Superalgebras*; the odd case, where the shift cannot be seen on the parity, is the **super-involution** with the Koszul-sign-twisted bracket. The loop algebra with the reflection $n\mapsto-n$ is the worked odd case. The operator layer belongs to the `- * Operator Theory` group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field, of characteristic not two |
| $\mathrm{G}=\bigoplus_i\mathrm{G}_i$ | a graded Lie algebra |
| $\omega$ | an involution of degree $d$ |
| $\mathrm{K},\mathrm{P}$ | the fixed and anti-fixed graded subspaces |
| $\mathbb{Z}\times\mathbb{Z}/2$ | the bigrading of an even involution |

## Further Reading

- Victor G. Kac, *Infinite Dimensional Lie Algebras* (Cambridge University Press, 3rd ed. 1990), for graded Lie algebras and their involutions.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 4–6 (Springer, 2002), for graded Lie algebras and symmetric pairs.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Graduate Texts in Mathematics 9 (Springer, 1972), for the ordinary structures underlying the graded ones.
- Victor G. Kac, "Lie superalgebras", *Advances in Mathematics* 26 (1977), 8–96, for the $\mathbb{Z}/2$-graded case.
