# __Symmetric Pairs and Cartan Pairs: the Reductivity Criterion__

## Introduction

**A decomposition of a Lie algebra into a subalgebra and a complement is a symmetric pair exactly when the complement is the $-1$ eigenspace of an involutive automorphism, and that condition is equivalent to one bracket inclusion: $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$.**

The article states the criterion and proves the implication that matters, applies it to the two complements of the antisymmetric half, and finds that the symmetric matrices pass while the upper triangular ones fail. It then adds the Cartan condition, the definiteness of $-B(X,\theta Y)$ on the algebra, computes the Killing form of $\mathfrak{gl}_n$ as $2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$, and verifies the definiteness on $\mathfrak{sl}_n$ for the involution $X\mapsto-X^{\mathsf T}$. It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric* for the closure rules and *$UT_n$ as the Complement of the Antisymmetric Part (Transpose Case)* for the failure of the triangular complement. It defers the group-level statements to *The Symmetric Space $\mathrm{GL}_n/O(n)$ and Its Complex Twin* and the form itself to *The Killing Form, Its Radical and the Triangular Case*.

## The Involution and the Eigenspaces

**The map $\theta(X)=-X^{\mathsf T}$ is an automorphism of the Lie algebra $\mathfrak{gl}_n(\mathbb{R})$, and it is an involution.** The transpose reverses the commutator, since

$$
[X,Y]^{\mathsf T}=(XY-YX)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}-X^{\mathsf T}Y^{\mathsf T}=-[X^{\mathsf T},Y^{\mathsf T}],
$$

so $\theta[X,Y]=-[X,Y]^{\mathsf T}=[X^{\mathsf T},Y^{\mathsf T}]=[\theta X,\theta Y]$. The map is linear, bijective and $\theta^{2}=\mathrm{id}$.

**Its eigenspaces are the two halves.** The $+1$ eigenspace is $\mathfrak{k}=\operatorname{Skew}_n=\mathfrak{so}(n)$ and the $-1$ eigenspace is $\mathfrak{p}=\operatorname{Sym}_n$, so

$$
\mathfrak{gl}_n(\mathbb{R})=\mathfrak{k}\oplus\mathfrak{p},\qquad \dim\mathfrak{k}=\frac{n(n-1)}{2},\quad \dim\mathfrak{p}=\frac{n(n+1)}{2}.
$$

A decomposition of this form, with $\mathfrak{k}$ the fixed set of an involutive automorphism, is a **symmetric pair**, written $(\mathfrak{gl}_n,\mathfrak{so}(n))$.

**Every symmetric pair obeys the three bracket rules.** From $\theta[X,Y]=[\theta X,\theta Y]$ and the eigenvalues, a bracket of two elements of sign $\epsilon$ and $\delta$ has sign $\epsilon\delta$:

$$
[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k},\qquad [\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p},\qquad [\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}.
$$

The first says that $\mathfrak{k}$ is a subalgebra, the second that $\mathfrak{p}$ is a module over it, the third that the complement is not a subalgebra. For the two halves of $M_n(\mathbb{R})$ the three rules are exactly the closure rules computed in *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric*.

## The Reductivity Criterion

**The three bracket rules are not independent, and the second is the criterion.** Suppose that $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$ with $\mathfrak{k}$ a subalgebra. Then the following are equivalent: $\mathfrak{p}$ is the $-1$ eigenspace of an involutive automorphism of $\mathfrak{g}$, and

$$
[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}.
$$

*Proof.* If $\theta$ is the automorphism and $\mathfrak{p}$ its $-1$ eigenspace, then for $X\in\mathfrak{k}$ and $P\in\mathfrak{p}$,

$$
\theta[X,P]=[\theta X,\theta P]=[X,-P]=-[X,P],
$$

so $[X,P]\in\mathfrak{p}$. Conversely, if the inclusion holds and $\mathfrak{k}$ is a subalgebra, the map that is $+1$ on $\mathfrak{k}$ and $-1$ on $\mathfrak{p}$ is an automorphism, because all three bracket rules hold.

**The criterion is called reductivity because it makes the complement a module.** When $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$, the adjoint action of $\mathfrak{k}$ on $\mathfrak{g}$ preserves $\mathfrak{p}$, so the complement carries a representation of the subalgebra, and $\mathfrak{k}$ is reductive in $\mathfrak{g}$. When the inclusion fails, the complement is a vector space and nothing more: it is not stable under the subalgebra, so no invariant of the pair can be read on it.

**The criterion can be tested with one bracket, and the test is exact.** There is no need to search for an involution: if the inclusion fails for a single pair $(X,P)$, no involutive automorphism has $\mathfrak{p}$ as its $-1$ eigenspace. The two complements of the antisymmetric half are therefore decided by a single computation each.

## The Two Complements Tested

**The symmetric half passes.** For $X$ antisymmetric and $P$ symmetric the commutator is symmetric, since

$$
[X,P]^{\mathsf T}=P^{\mathsf T}X^{\mathsf T}-X^{\mathsf T}P^{\mathsf T}=PX-XP=-[X,P],
$$

so the sign is the opposite one and $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$ holds. Hence $(\mathfrak{gl}_n,\mathfrak{so}(n))$ is a symmetric pair with $\mathfrak{p}=\operatorname{Sym}_n$, and the third rule $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$ holds as well: the commutator of two symmetric matrices is antisymmetric.

**The triangular algebra fails.** Take $X=E_{12}-E_{21}$, which is anti-Hermitian, and $P=E_{12}$, which is upper triangular. Then

$$
[X,P]=E_{12}E_{12}-E_{12}E_{21}-E_{21}E_{12}+E_{21}E_{21}
=E_{22}-E_{11}+0+0,
$$

which is diagonal and not strictly upper triangular, so $[X,P]\notin UT_n$; the computation at $n=2,3,4$ produces a non-triangular entry every time. Hence no involutive automorphism of $\mathfrak{gl}_n$ has $UT_n$ as its $-1$ eigenspace, and the decomposition $\mathfrak{gl}_n=\mathfrak{so}(n)\oplus UT_n$ is not a symmetric pair.

**The failure is caused by the diagonal.** The diagonal part of $UT_n$ is what the bracket produces, and a complement that contains the diagonal together with a nilpotent part cannot be stable: the bracket of the antisymmetric part with the nilpotent part returns to the diagonal. The symmetric half also contains the diagonal, but its off-diagonal part is symmetric rather than triangular, and the symmetry is exactly what makes the sign work.

**The criterion also separates the two complements in dimension.** Both have dimension $n(n+1)/2$, both are complements of $\mathfrak{so}(n)$, and only one carries a representation of $\mathfrak{so}(n)$. So the dimension of a complement is not the information that matters; the bracket is.

## The Cartan Form

**A Cartan pair is a symmetric pair whose form is definite.** Let $\theta$ be an involutive automorphism of a semisimple algebra and $B$ the Killing form. Then $\theta$ is a **Cartan involution** when

$$
B_{\theta}(X,Y)=-B(X,\theta Y)
$$

is positive definite, and the pair $(\mathfrak{g},\mathfrak{k})$ is then a **Cartan pair**. The form $B_{\theta}$ is symmetric, invariant and positive definite on the whole algebra, and the decomposition is orthogonal for it; the Killing form $B$ itself is negative definite on $\mathfrak{k}$ and positive definite on $\mathfrak{p}$.

**The Killing form of $\mathfrak{gl}_n$ is $2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$.** Building the adjoint matrices in the basis of units and taking traces gives

$$
B(X,Y)=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y),
$$

verified at $n=2,3$. On the traceless part the second term vanishes and $B(X,Y)=2n\operatorname{tr}(XY)$, which is the Killing form of $\mathfrak{sl}_n$.

**The involution $\theta(X)=-X^{\mathsf T}$ is a Cartan involution of $\mathfrak{sl}_n$.** On the traceless part,

$$
B_{\theta}(X,X)=-B(X,\theta X)=-2n\operatorname{tr}(X\cdot(-X^{\mathsf T}))=2n\operatorname{tr}(XX^{\mathsf T})=2n\sum_{ij}X_{ij}^{2}>0
$$

for $X\neq0$. The computation at $n=2,3,4$ gives a positive value in every case. So $(\mathfrak{sl}_n,\mathfrak{so}(n))$ is a Cartan pair, and the definite form is $2n$ times the trace form. On all of $\mathfrak{gl}_n$ the same involution is not a Cartan involution for the Killing form, because of the trace term; the trace form itself, with the same involution, is definite, and that is the form the corpus uses.

## The Case $n=2$

**At $n=2$ the pair is $(\mathfrak{gl}_2,\mathfrak{so}(2))$ with dimensions $4=1+3$.** The subalgebra is the line $\mathbb{R}J$, the complement is the three-dimensional space spanned by $\mathrm{I},\sigma_1,\sigma_3$, and the three bracket rules read

$$
[\mathfrak{k},\mathfrak{k}]=0,\qquad [\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}\ \text{of dimension }2,\qquad [\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k},
$$

the middle image is spanned by $\sigma_1$ and $\sigma_3$, since $[J,\sigma_1]=-2\sigma_3$ and $[J,\sigma_3]=2\sigma_1$, and the last holds because the commutator of two symmetric matrices is a multiple of $J$, which the computation confirms by producing a rank-one answer in the direction $J$.

**The triangular complement fails already at $n=2$.** With $X=J$ and $P=E_{12}$ the commutator is $E_{22}-E_{11}$, which is diagonal and therefore not in $UT_2$. The failure at the smallest case is the same failure as at every case, and it cannot be repaired by choosing a different complement of dimension $3$: the criterion tests a bracket, and the bracket of the anti-Hermitian line with the triangular algebra always reaches the diagonal.

**The Cartan form at $n=2$ is the Euclidean form on three dimensions.** Since $\mathfrak{sl}_2$ is three-dimensional and $\mathfrak{so}(2)$ is one-dimensional, the complement is two-dimensional and the definite form is $4\sum X_{ij}^{2}$ on the traceless part. The biquaternion reading of the pair is the one of *Coda: $n=2$ and the Biquaternion Algebra*: the subalgebra is the rotation direction, the complement the two stretch directions, and the pair is the model of every later symmetric space.

## Summary

The map $\theta(X)=-X^{\mathsf T}$ is an involutive automorphism of $\mathfrak{gl}_n$ with fixed set $\mathfrak{so}(n)$ and anti-fixed set $\operatorname{Sym}_n$, so $(\mathfrak{gl}_n,\mathfrak{so}(n))$ is a symmetric pair with the bracket rules $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$, $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$ and $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$. The second rule is the criterion: a complement is the anti-fixed set of an involution exactly when it is stable under the subalgebra. The symmetric half passes, since the commutator of an antisymmetric with a symmetric matrix is symmetric; the triangular algebra fails, since the commutator of an antisymmetric matrix with $E_{12}$ reaches the diagonal. The Killing form of $\mathfrak{gl}_n$ is $2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$, and $-B(X,\theta X)=2n\operatorname{tr}(XX^{\mathsf T})$ is positive on $\mathfrak{sl}_n$, so the pair is a Cartan pair.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\theta(X)=-X^{\mathsf T}$ | the involutive automorphism that gives the pair |
| $\mathfrak{k}=\operatorname{Skew}_n=\mathfrak{so}(n)$ | the fixed subalgebra, of dimension $n(n-1)/2$ |
| $\mathfrak{p}=\operatorname{Sym}_n$ | the anti-fixed complement, of dimension $n(n+1)/2$ |
| $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$ | the reductivity criterion |
| $B_{\theta}(X,Y)=-B(X,\theta Y)$ | the Cartan form |
| $B(X,Y)=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$ | the Killing form of $\mathfrak{gl}_n$ |
| $(\mathfrak{gl}_n,\mathfrak{so}(n))$ | the symmetric pair, a Cartan pair on $\mathfrak{sl}_n$ |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Geometric Analysis* (AMS, 2001), for symmetric pairs, Cartan involutions and the Cartan decomposition.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2002), for the reductivity criterion and the definite form $B_\theta$.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the Killing form of $\mathfrak{gl}_n$ and $\mathfrak{sl}_n$.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric.html), for the bracket rules that the pair obeys.
- [$UT_n$ as the Complement of the Antisymmetric Part (Transpose Case)](utn-as-the-complement-of-the-antisymmetric-part-transpose-case.html), for the complement that fails the criterion.
- [The Two Halves as Orthogonal Complements](the-two-halves-as-orthogonal-complements.html), for the orthogonality that the Cartan form makes definite.
