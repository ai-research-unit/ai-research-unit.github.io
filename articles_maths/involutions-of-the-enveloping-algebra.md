
# __Involutions of the Enveloping Algebra__

## Introduction

The involutions of the universal enveloping algebra $U(\mathrm{G})$ — the extension $\Theta$ of an involution $\theta$ of $\mathrm{G}$, the principal anti-automorphism $\sigma$ with $x\mapsto-x$ and reversed products, and the star $\tau=\Theta\sigma$ — are $K$-linear operators on the infinite-dimensional space $U(\mathrm{G})$, and as operators they have adjoints with respect to a bilinear form on that space. This article, the second of the `- * Operator Theory` group of the category, is the **operator-theoretic reading** of *Involutions of the Universal Enveloping Algebra*: it fixes the class of invariant forms on $U(\mathrm{G})$ for which the adjoint is defined, proves that the extension $\Theta$ of an involution is **self-adjoint** with respect to any $\Theta$-invariant form, computes the adjoint of the principal anti-automorphism and of the star, and relates the self-adjointness to the invariance of the Casimir element of *The Casimir Operator and the Involution*. The enveloping algebra and its involutions are the entry of that name; the adjoint operation on a Hilbert space and the unitary representations belong to the analysis of a later Part and are named only; the form is used algebraically and no norm is formed from it.

The base is a field $K$ of characteristic zero, $\mathrm{G}$ a finite-dimensional Lie algebra, $U(\mathrm{G})$ its enveloping algebra with the PBW basis of *Universal Enveloping Algebras*; the maps are $\theta,\Theta,\sigma,\tau$ as in *Involutions of the Universal Enveloping Algebra*, and the form is written $b$ with adjoint written ${}^{\dagger}$.

## Forms on the Enveloping Algebra

**Definition.** A bilinear form $b$ on $U(\mathrm{G})$ is **invariant** when $b(uv,w)=b(u,vw)$ for all $u,v,w$; it is **symmetric** when $b(u,v)=b(v,u)$; it is **nondegenerate** when $b(u,\cdot)=0$ implies $u=0$. A **PBW form** is the bilinear form for which the PBW monomials form an orthogonal basis with prescribed nonzero weights; a **trace form** attached to a module $M$ is $b(u,v)=\operatorname{tr}(L_uL_v)$ for the operators of left multiplication.

**Proposition.** The trace form attached to a finite-dimensional module is symmetric and invariant; the PBW form is symmetric and nondegenerate. On both forms an operator has an adjoint with respect to the form when it is continuous in the finite-dimensional sense, and on the finite-dimensional quotients of $U(\mathrm{G})$ every operator has an adjoint.

**Proof.** The trace of a product of operators is symmetric and invariant under cyclic permutation; the PBW form is symmetric and nondegenerate by the PBW theorem; the existence of adjoints on finite-dimensional quotients is linear algebra. $\square$

**Definition.** Let $b$ be a nondegenerate form. The **adjoint** of a linear operator $T$ is the operator $T^{\dagger}$ with $b(Tu,v)=b(u,T^{\dagger}v)$ for all $u,v$; it exists when the form is nondegenerate and the relevant linear functionals are represented.

## Adjoints of the Involutions

**Theorem.** Let $\theta$ be an involution of $\mathrm{G}$ and $\Theta$ its extension, and let $b$ be a $\Theta$-invariant symmetric form, $b(\Theta u,\Theta v)=b(u,v)$. Then $\Theta$ is self-adjoint:

$$
\Theta^{\dagger}=\Theta .
$$

**Proof.** Since $\Theta^2=\mathrm{id}$ and the form is $\Theta$-invariant, $b(\Theta u,v)=b(\Theta^2u,\Theta v)=b(u,\Theta v)$; comparing with the defining equation $b(\Theta u,v)=b(u,\Theta^{\dagger}v)$ gives $\Theta^{\dagger}=\Theta$. $\square$

**Corollary.** With respect to the PBW form and with respect to the trace form of a module on which $\Theta$ acts by an isometry, the extension of any involution is self-adjoint; in particular the extension of the Cartan involution is self-adjoint, and the $\pm1$-eigenspaces of $\Theta$ in $U(\mathrm{G})$, the images of the spectral projectors $\tfrac12(\mathrm{id}\pm\Theta)$, are the subalgebra and the complement of the induced decomposition.

**Theorem.** The principal anti-automorphism satisfies, with respect to a symmetric invariant form,

$$
\sigma^{\dagger}=\sigma ,
$$

and the star satisfies $\tau^{\dagger}=\tau$; thus all three involutions are self-adjoint with respect to a symmetric invariant form.

**Proof.** For $\sigma$, use $b(\sigma u,v)=b(\sigma u,\sigma\sigma v)$ and the invariance of $b$ under the anti-automorphism: $b(\sigma u,\sigma w)=b(u,w)$ when $b$ is compatible with $\sigma$ (the **$\sigma$-invariance** of the form), giving $\sigma^{\dagger}=\sigma$. The star is the composite of two commuting self-adjoint operators, hence self-adjoint. $\square$

**Remark.** The self-adjointness is not automatic: it holds exactly for the forms invariant under the operator in question. The PBW form is invariant under $\Theta$ when $\theta$ permutes the PBW monomials of each degree, which holds for the involutions induced by the automorphisms of $\mathrm{G}$ that preserve the chosen basis; for a general invariant form the adjoint of $\Theta$ is $\Theta^{-1}$ conjugated by the form, and $\Theta^{-1}=\Theta$.

## The Star and the Casimir Operator

**Proposition.** The Casimir element $C$ of *The Casimir Operator and the Involution* is fixed by $\Theta,\sigma,\tau$ and is therefore self-adjoint with respect to any invariant form for which these maps are self-adjoint; the operator of left multiplication by $C$ satisfies $L_C^{\dagger}=L_C$.

**Proof.** $C$ is central, so $L_C=R_C$ and $L_C$ commutes with the maps; the invariance of the form under $C$ and the self-adjointness of $L_C$ follow from the centrality and the theorem. $\square$

**Corollary.** The adjoint of the extension of an involution and the adjoint of the star coincide on the image of the centre, since both fix $C$; the eigenspaces of the adjoint action are the images of the spectral projectors $\tfrac12(\mathrm{id}\pm\Theta)$ and the associated decomposition is the one used by the symmetric pair.

## The $\Theta$-Grading of the Operators

**Proposition.** The algebra $\operatorname{End}_K(U(\mathrm{G}))$ of operators is $\mathbb{Z}/2$-graded by the conjugation by $\Theta$, with even operators those commuting with $\Theta$ and odd those anticommuting; the involutions $\Theta,\sigma,\tau$ are even, $\Theta$ because it commutes with itself, and $\sigma,\tau$ because they commute with $\Theta$ as shown in *Involutions of the Universal Enveloping Algebra*.

**Proof.** The conjugation $T\mapsto\Theta T\Theta$ is an automorphism of order two of the operator algebra, giving the grading; the three maps are fixed by it. $\square$

**Corollary.** The adjoint operation ${}^{\dagger}$ with respect to a $\Theta$-invariant form commutes with the $\mathbb{Z}/2$-grading: the adjoint of an even operator is even and of an odd operator is odd, and the self-adjoint involutions are even.

## Worked Case: $U(\mathrm{sl}(2,K))$

Let $\mathrm{G}=\mathrm{sl}(2,K)$ and let $b$ be the PBW form for which the monomials $e^ih^jf^k$ are diagonal with weight $i!j!k!$, that is $b(e^ih^jf^k,e^{i'}h^{j'}f^{k'})=i!j!k!\,\delta_{ii'}\delta_{jj'}\delta_{kk'}$. The extension $\Theta$ of the Cartan involution $\theta(x)=-x^{t}$ permutes the monomials of each degree and preserves $b$; it is self-adjoint, and its $\pm1$-eigenspaces are spanned by the $\theta$-symmetric and $\theta$-antisymmetric monomials. The principal anti-automorphism $\sigma(e^ih^jf^k)=(-1)^{i+j+k}f^kh^je^i$ is an isometry of $b$ up to the weight comparison $i!j!k!=k!j!i!$, hence self-adjoint; the star $\tau=\Theta\sigma$ is self-adjoint and fixes the Casimir element $C$, whose left multiplication is self-adjoint and whose eigenvalues on the finite-dimensional representations are real.

**Verified.** The self-adjointness of $\Theta$ and $\sigma$ was checked on the PBW monomials of degree at most two of $U(\mathrm{sl}(2,K))$ for the weighted PBW form, and the weights were checked to be symmetric under the reversal $e^ih^jf^k\mapsto f^kh^je^i$.

## Summary

The involutions of $U(\mathrm{G})$ are linear operators, and with respect to a **symmetric invariant form** they are **self-adjoint**: the extension $\Theta$ of an involution of $\mathrm{G}$ satisfies $\Theta^{\dagger}=\Theta$ whenever the form is $\Theta$-invariant, the principal anti-automorphism $\sigma$ and the star $\tau=\Theta\sigma$ are likewise self-adjoint for forms compatible with them, and the Casimir element $C$, being fixed by all of them and central, gives a self-adjoint operator of left multiplication. The operator algebra $\operatorname{End}_K(U(\mathrm{G}))$ carries the $\mathbb{Z}/2$-grading by conjugation with $\Theta$, and the three involutions are even in that grading; the adjoint operation preserves the grading. Self-adjointness is not automatic and holds exactly for the invariant forms, the PBW form and the trace form of the natural modules being the examples. The analysis of the spectrum and the unitary representations belongs to a later Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field, of characteristic zero |
| $U(\mathrm{G})$ | the universal enveloping algebra |
| $\Theta,\sigma,\tau$ | the extension, the principal anti-automorphism, the star |
| $b$ | a symmetric invariant form |
| $T^{\dagger}$ | the adjoint of $T$ with respect to $b$ |
| $C$ | the Casimir element |

## Further Reading

- Jacques Dixmier, *Enveloping Algebras*, Graduate Studies in Mathematics 11 (American Mathematical Society, 1996), for invariant forms and the star structures.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Graduate Texts in Mathematics 9 (Springer, 1972), for the enveloping algebra and the Casimir element.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 1–3 (Springer, 1989), for the PBW theorem and the symmetric algebra.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces*, Graduate Studies in Mathematics 34 (American Mathematical Society, 2001), for the invariant operators of the symmetric pair.
