# __Symmetric Pairs and Cartan Pairs: the Reductivity Criterion over $\mathbb{R}$__

## Introduction

**An involution of a Lie algebra splits it into a fixed part and an anti-fixed part with the bracket rules $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$, $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$ and $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$, and the involution $\theta(X)=-X^{\mathsf T}$ of $\mathfrak{gl}_n(\mathbb{R})$ gives the pair $\mathfrak{k}=\mathfrak{so}(n)$, $\mathfrak{p}=\operatorname{Sym}_n$.**

The article proves the three bracket rules, works the two standard examples, states the reductivity criterion, computes the Killing forms of $\mathfrak{gl}_n(\mathbb{R})$, $\mathfrak{so}(n)$ and $\mathfrak{sl}_n(\mathbb{R})$ with their signatures, and closes with the Cartan pair of the first kind. It assumes *The Two Halves: Symmetric and Antisymmetric* and *The Two Halves as Orthogonal Complements for the Trace Form* for the two halves and the trace form, and *The Triangular Decomposition $h\oplus n_+\oplus n_-$* for the bracket that fails the third rule.

## The Involution of a Lie Algebra

**Definition.** An involution of a Lie algebra $\mathfrak{g}$ is a linear map $\theta:\mathfrak{g}\to\mathfrak{g}$ with $\theta^{2}=\mathrm{id}$ and

$$
\theta([X,Y])=[\theta X,\theta Y]
$$

for all $X,Y\in\mathfrak{g}$.

**The map is an automorphism of the Lie algebra, though the transpose reverses the matrix product.** This is the difference from the earlier articles: the transpose is an anti-automorphism of the associative algebra and an automorphism of the Lie algebra, since

$$
\theta([X,Y])=-(XY-YX)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}-X^{\mathsf T}Y^{\mathsf T}=[X^{\mathsf T},Y^{\mathsf T}]=[\theta X,\theta Y].
$$

So the same map reverses one product and preserves the other, and the theory of this article uses the second.

**The eigenvalues are $\pm1$ and the eigenspaces are the two halves.** Since $\theta^{2}=\mathrm{id}$, the eigenvalues lie in $\{1,-1\}$, and

$$
\mathfrak{k}=\{X:\theta X=X\},\qquad \mathfrak{p}=\{X:\theta X=-X\}.
$$

**The decomposition is a direct sum.** Every $X$ equals $\tfrac12(X+\theta X)+\tfrac12(X-\theta X)$, a fixed and an anti-fixed part, and the two eigenspaces meet only at zero.

## The Three Bracket Rules

**Theorem.** With $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$ as above,

$$
[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k},\qquad [\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p},\qquad [\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}.
$$

*Proof.* Apply $\theta$ to the bracket. If $X,Y\in\mathfrak{k}$ then $\theta[X,Y]=[\theta X,\theta Y]=[X,Y]$, so the bracket is fixed. If $X\in\mathfrak{k}$ and $Y\in\mathfrak{p}$ then $\theta[X,Y]=[X,-Y]=-[X,Y]$, so the bracket is anti-fixed. If $X,Y\in\mathfrak{p}$ then $\theta[X,Y]=[-X,-Y]=[X,Y]$, so the bracket is fixed.

**The first two rules say that $\mathfrak{k}$ is a subalgebra and that $\mathfrak{p}$ is a module for it.** The third is the one that distinguishes a symmetric pair from a general decomposition: the bracket of two elements of the complement returns to the subalgebra.

**The third rule fails for the triangular decomposition.** In *The Triangular Decomposition $h\oplus n_+\oplus n_-$* the pieces $n_+$ and $n_-$ satisfy $[n_+,n_-]\not\subseteq h$, with a diagonal shadow of dimension $n-1$ and a total span of dimension $1$, $6$, $13$ at $n=2,3,4$. The triangular picture is not symmetric.

## The Example $\theta(X)=-X^{\mathsf T}$

**The map is an involution of $\mathfrak{gl}_n(\mathbb{R})$.** Measured on $100$ random pairs at each of $n=2,3,4$, the identity $\theta([X,Y])=[\theta X,\theta Y]$ held in $100$ cases out of $100$.

**The two eigenspaces are the two halves of the first article.**

$$
\mathfrak{k}=\operatorname{Skew}_n=\mathfrak{so}(n),\qquad \mathfrak{p}=\operatorname{Sym}_n,
$$

of dimensions $n(n-1)/2$ and $n(n+1)/2$.

**The three rules are the three product facts.** $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$ says that the commutator of two skew matrices is skew. $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$ says that the commutator of a skew and a symmetric matrix is symmetric: measured, $100$ of $100$ random pairs at $n=2,3$. $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$ says that the commutator of two symmetric matrices is skew, the measured $100$ of $100$ at $n=2,3$.

**The last rule is the one with the sign.** For symmetric $S,T$,

$$
[S,T]^{\mathsf T}=(ST-TS)^{\mathsf T}=T^{\mathsf T}S^{\mathsf T}-S^{\mathsf T}T^{\mathsf T}=TS-ST=-[S,T],
$$

so the commutator is skew. The same computation with the Jordan product gives a symmetric result, which is why the symmetric half is a Jordan algebra under the anticommutator and a Lie algebra only after the bracket is taken.

## The Block Diagonal Sign

**Definition.** Let $D=\operatorname{diag}(\mathrm{I}_p,-\mathrm{I}_q)$ with $p+q=n$ and put $\theta(X)=DXD^{-1}=DXD$.

**The map is an involution of $\mathfrak{gl}_n(\mathbb{R})$.** $D^{2}=\mathrm{I}$, so $\theta^{2}=\mathrm{id}$, and conjugation is an automorphism of the associative algebra, hence of the Lie algebra.

**The two eigenspaces are the block diagonal and the off-diagonal parts.** Write $X$ in blocks $X=\begin{pmatrix}A&B\\ C&E\end{pmatrix}$ with $A$ of size $p$ and $E$ of size $q$. Then

$$
\theta(X)=\begin{pmatrix}A&-B\\ -C&E\end{pmatrix},
$$

so $\mathfrak{k}$ is the set of block diagonal matrices with $B=C=0$ and $\mathfrak{p}$ is the set of matrices with $A=E=0$.

**The dimensions are $p^{2}+q^{2}$ and $2pq$, and they add to $n^{2}$.** Measured at $p=2$, $q=3$, they are $13$ and $12$, summing to $25$. The three rules held in $100$ of $100$ random tests.

**The subalgebra $\mathfrak{k}$ is $\mathfrak{gl}_p(\mathbb{R})\oplus\mathfrak{gl}_q(\mathbb{R})$, which is reductive and not semisimple.** The complement consists of the two rectangular blocks, and the bracket of two such blocks lands in $\mathfrak{k}$ as the third rule requires.

## The Reductivity Criterion

**Definition.** A Lie algebra is reductive when its adjoint representation is completely reducible, equivalently when it is the direct sum of its centre and a semisimple ideal.

**Theorem (reductivity criterion).** Let $\theta$ be an involution of $\mathfrak{g}$ with fixed algebra $\mathfrak{k}$. Then $\mathfrak{k}$ is a subalgebra, $\mathfrak{p}$ is a $\mathfrak{k}$-module, and if $\mathfrak{g}$ has a nondegenerate invariant form $B$ with $B(\theta X,\theta Y)=B(X,Y)$, then $\mathfrak{p}=\mathfrak{k}^{\perp}$, $B|_{\mathfrak{k}}$ is nondegenerate, and $\mathfrak{k}$ is reductive with $\mathfrak{p}$ a completely reducible $\mathfrak{k}$-module.

*Proof of the orthogonality.* For $X\in\mathfrak{k}$ and $Y\in\mathfrak{p}$,

$$
B(X,Y)=B(\theta X,\theta Y)=B(X,-Y)=-B(X,Y),
$$

so $B(X,Y)=0$. Nondegeneracy gives $\dim\mathfrak{k}^{\perp}=n^{2}-\dim\mathfrak{k}=\dim\mathfrak{p}$ in the matrix case, hence $\mathfrak{p}=\mathfrak{k}^{\perp}$, and the restriction of a nondegenerate form to a space whose orthogonal complement is a complement is nondegenerate.

**The invariance is automatic for the Killing form.** An automorphism preserves $B$, since $\operatorname{ad}(\theta X)=\theta\operatorname{ad}(X)\theta^{-1}$ and the trace is conjugation-invariant.

**Complete reducibility is the remaining step.** For $\mathfrak{k}=\mathfrak{so}(n)$ it follows from compactness: the group $\mathrm{O}(n)$ is compact, an invariant inner product exists on $\mathfrak{gl}_n(\mathbb{R})$ by averaging, and the orthogonal complement of an invariant subspace is invariant. For a general pair the same conclusion is a theorem of Mostow, and it is the standard proof that the fixed algebra of an involution of a semisimple Lie algebra is reductive.

## The Killing Form and Cartan's Criterion

**Definition.** For a finite-dimensional Lie algebra $\mathfrak{g}$,

$$
B(X,Y)=\operatorname{tr}(\operatorname{ad}X\circ\operatorname{ad}Y).
$$

**The form is symmetric, invariant and preserved by every automorphism.** Symmetry comes from the trace, invariance from $\operatorname{ad}[X,Y]=[\operatorname{ad}X,\operatorname{ad}Y]$, and preservation from $\operatorname{ad}(\theta X)=\theta\operatorname{ad}(X)\theta^{-1}$.

**Cartan's criterion.** $\mathfrak{g}$ is semisimple if and only if $B$ is nondegenerate, and solvable if and only if $B(\mathfrak{g},[\mathfrak{g},\mathfrak{g}])=0$. The signature decides compactness.

**On $\mathfrak{gl}_n(\mathbb{R})$ the Killing form is**

$$
B(X,Y)=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y).
$$

Verified against $\operatorname{tr}(\operatorname{ad}X\operatorname{ad}Y)$ on the matrix-unit basis at $n=2,3$, the two expressions agree entry by entry.

## The Killing Form of $\mathfrak{so}(n)$

**Proposition.** For $X,Y\in\mathfrak{so}(n)$,

$$
B(X,Y)=(n-2)\operatorname{tr}(XY).
$$

**Measured, the form is negative definite for $n\ge3$.** The eigenvalues are $-2$, each with multiplicity $3$, at $n=3$, and $-4$, each with multiplicity $6$, at $n=4$. Both agree with the formula: $(3-2)\cdot(-2)=-2$ and $(4-2)\cdot(-2)=-4$, and the multiplicity is the dimension $n(n-1)/2$.

**Negative definiteness is compactness.** A real Lie algebra whose Killing form is negative definite is the Lie algebra of a compact group, and here the group is $\mathrm{O}(n)$. Cartan's criterion then gives the semisimplicity of $\mathfrak{so}(n)$ for $n\ge3$.

**The exception is $n=2$.** $\mathfrak{so}(2)$ is one-dimensional and abelian, so its Killing form is zero and the proposition reduces to $0=0$.

## The Killing Form of $\mathfrak{sl}_n(\mathbb{R})$

**Proposition.** For $X,Y\in\mathfrak{sl}_n(\mathbb{R})$, $B(X,Y)=2n\operatorname{tr}(XY)$, and the signature is $(n^{2}-1-n(n-1)/2,\ n(n-1)/2)$.

**Measured, the signatures are $(2,1)$, $(5,3)$, $(9,6)$ at $n=2,3,4$.** Both counts grow like $n^{2}/2$, so the form is indefinite at every order and $\mathfrak{sl}_n(\mathbb{R})$ is semisimple and not compact.

**The negative directions are the skew part.** On $\operatorname{Skew}_n$ the trace form is negative definite and the Killing form is a positive multiple of it, so the compact directions are exactly the antisymmetric ones.

## The Cartan Pair of the First Kind

**The pair $(\mathfrak{gl}_n(\mathbb{R}),\mathfrak{so}(n))$ with $\mathfrak{p}=\operatorname{Sym}_n$ is a Cartan pair.** The three bracket rules hold, $\mathfrak{k}$ is compact, and $\mathfrak{p}=\mathfrak{k}^{\perp}$ for both the trace form and the Killing form.

**The symmetric space is the space of positive definite matrices.** The quotient $\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)$ has dimension $n(n+1)/2=\dim\mathfrak{p}$, and the exponential map $\exp:\operatorname{Sym}_n\to P_n$ is a bijection. Measured on $100$ random symmetric matrices at $n=2,3$, the exponential was positive definite in $100$ cases out of $100$.

**The pair is of the first kind.** $\mathfrak{gl}_n(\mathbb{R})$ carries no $\operatorname{ad}$-invariant complex structure: its centre is $\mathbb{R}\mathrm{I}$, of odd real dimension one. So the pair is not of the complex type.

## Summary

An involution $\theta$ of a Lie algebra with $\theta^{2}=\mathrm{id}$ splits it as $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$, and the three bracket rules $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$, $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$, $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$ follow from applying $\theta$ to the bracket. For $\theta(X)=-X^{\mathsf T}$ on $\mathfrak{gl}_n(\mathbb{R})$ the parts are $\mathfrak{k}=\mathfrak{so}(n)=\operatorname{Skew}_n$ and $\mathfrak{p}=\operatorname{Sym}_n$, and the three rules held in $100$ of $100$ random tests. For $\theta=\mathrm{Ad}(\operatorname{diag}(\mathrm{I}_p,-\mathrm{I}_q))$ the parts have dimensions $p^{2}+q^{2}$ and $2pq$, measured $13$ and $12$ at $p=2$, $q=3$. The reductivity criterion makes $\mathfrak{k}$ reductive and $\mathfrak{p}$ a completely reducible module, with $\mathfrak{p}=\mathfrak{k}^{\perp}$ for any invariant nondegenerate form. The Killing form is $2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$ on $\mathfrak{gl}_n(\mathbb{R})$, negative definite on $\mathfrak{so}(n)$ with eigenvalues $-2$ thrice at $n=3$ and $-4$ six times at $n=4$, and of signature $(2,1)$, $(5,3)$, $(9,6)$ on $\mathfrak{sl}_n(\mathbb{R})$ at $n=2,3,4$. The pair $(\mathfrak{gl}_n(\mathbb{R}),\mathfrak{so}(n))$ is a Cartan pair of the first kind, and its symmetric space is the space of positive definite matrices.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\theta$ | an involution of a Lie algebra, $\theta^{2}=\mathrm{id}$, $\theta[X,Y]=[\theta X,\theta Y]$ |
| $\mathfrak{k}$ | the fixed algebra of $\theta$, the $+1$ eigenspace |
| $\mathfrak{p}$ | the anti-fixed space, the $-1$ eigenspace, the complement |
| $\mathfrak{so}(n)$ | $\operatorname{Skew}_n$, the compact part for $\theta(X)=-X^{\mathsf T}$ |
| $\operatorname{Sym}_n$ | the complement, the space of the symmetric space |
| $B(X,Y)=\operatorname{tr}(\operatorname{ad}X\operatorname{ad}Y)$ | the Killing form |
| $P_n$ | the positive definite matrices, the symmetric space $\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)$ |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for symmetric spaces and Cartan pairs.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2002), for involutions, real forms and the Killing form.
- [The Two Halves: Symmetric and Antisymmetric](the-two-halves-symmetric-and-antisymmetric-over-r.html), for the two halves and their products.
- [The Two Halves as Orthogonal Complements for the Trace Form](the-two-halves-as-orthogonal-complements-for-the-trace-form.html), for the signature of the trace form.
- [The Triangular Decomposition $h\oplus n_+\oplus n_-$](the-triangular-decomposition-h-n-plus-n-minus-of-mnr.html), for the decomposition that fails the third rule.
