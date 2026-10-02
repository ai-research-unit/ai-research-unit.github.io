
# __The Casimir Operator__

## Introduction

The **Casimir element** of a semisimple Lie algebra $\mathrm{G}$ is the central element $C=\sum_i x_i x^i$ of the universal enveloping algebra $U(\mathrm{G})$, formed from a basis and its dual basis with respect to the Killing form. It is defined, and it is proved to be central and to act on an irreducible module by the scalar $(\lambda,\lambda+2\rho)$, in *Representations of Lie Algebras*; the element, its centrality and its eigenvalue are owned by that article and are cited here. This article treats the **operator** that the element induces. In each representation $\pi$ the element gives the operator $\Omega_\pi=\pi(C)=\sum_i\pi(x_i)\pi(x^i)$, and in the regular representation it gives left multiplication by $C$ on $U(\mathrm{G})$; the operator is a $\mathrm{G}$-module endomorphism, its eigenspaces are the isotypic components of a completely reducible module, it is the identity on the adjoint module up to the normalisation fixed by the Killing form, and its behaviour on tensor products is governed by a mixed term.

The universal enveloping algebra, its filtration and the Poincaré–Birkhoff–Witt theorem are *Universal Enveloping Algebras*; the modules, the weights, the highest weight classification and the Casimir element are *Representations of Lie Algebras*; the Cartan subalgebra, the roots and the Killing form are *Root Systems and Classification* and *The Killing Form Operator*. Nothing owned by those entries is re-derived.

The article stays inside Part I: the operator is algebraic, and its analytic reading as a Laplace operator on a manifold, its spectrum and its heat kernel belong to Part II and Part III and are not used. The base is an algebraically closed field $K$ of characteristic zero, and $\mathrm{G}$ is a finite-dimensional semisimple Lie algebra over $K$; the notation of the root system is that of *Root Systems and Classification*, and the Casimir element is written $C$ while its operator on a representation is written $\Omega_\pi$.

## The Casimir Operator of a Representation

### The Definition, Recalled

**Definition.** Let $(x_1,\dots,x_m)$ be a basis of $\mathrm{G}$ and let $(x^1,\dots,x^m)$ be the dual basis with respect to the Killing form, $\kappa(x_i,x^j)=\delta_i^j$. The **Casimir element** is $C=\sum_i x_ix^i\in U(\mathrm{G})$; it is independent of the choice of basis and central. These statements, with the centrality of $C$ and the eigenvalue $(\lambda,\lambda+2\rho)$ on the irreducible module $V(\lambda)$, are from *Representations of Lie Algebras*.

**Definition.** For a representation $\pi:\mathrm{G}\to\operatorname{End}_K(V)$ the **Casimir operator** is

$$
\Omega_\pi=\pi(C)=\sum_{i=1}^{m}\pi(x_i)\,\pi(x^i)\in\operatorname{End}_K(V).
$$

The assignment is functorial: if $f:V\to W$ is a homomorphism of $\mathrm{G}$-modules then $f\circ\Omega_\pi=\Omega_{\pi}\circ f$, because $f$ intertwines the operators $\pi(x)$.

### Independence of the Basis

**Proposition.** The operator $\Omega_\pi$ does not depend on the basis: for any basis $(y_1,\dots,y_m)$ with dual basis $(y^1,\dots,y^m)$, $\sum_i\pi(y_i)\pi(y^i)=\sum_i\pi(x_i)\pi(x^i)$.

**Proof.** This is the basis-independence of the Casimir element, transported by the algebra homomorphism $\pi$ that the universal property of $U(\mathrm{G})$ supplies; the operator statement is the image of the element statement. $\square$

### Centrality as an Operator

**Theorem (the Casimir operator is an intertwining operator).** For every $x\in\mathrm{G}$,

$$
[\Omega_\pi,\pi(x)]=0,
$$

so $\Omega_\pi\in\operatorname{End}_{\mathrm{G}}(V)$, the algebra of $\mathrm{G}$-module endomorphisms of $V$.

**Proof.** The centrality of $C$ in $U(\mathrm{G})$ gives $[C,x]=0$ for the image of $x$ in $U(\mathrm{G})$, and $\pi$ is an algebra homomorphism, so $[\pi(C),\pi(x)]=0$. $\square$

**Corollary (preservation, restriction and descent).** The operator $\Omega_\pi$ preserves every submodule and descends to every quotient; on a direct sum of representations it acts componentwise; and if $V$ is irreducible then $\Omega_\pi$ is a scalar, by Schur's lemma, with the scalar $(\lambda,\lambda+2\rho)$ for $V=V(\lambda)$.

## The Isotypic Decomposition

### Distinct Highest Weights Give Distinct Eigenvalues

**Proposition.** The map $\lambda\mapsto(\lambda,\lambda+2\rho)=(\lambda+\rho,\lambda+\rho)-(\rho,\rho)$ is injective on the dominant integral weights.

**Proof.** If $(\lambda+\rho,\lambda+\rho)=(\mu+\rho,\mu+\rho)$ then $\lambda+\rho$ and $\mu+\rho$ have the same length; both lie in the same open Weyl chamber, since $\lambda+\rho$ and $\mu+\rho$ are strictly dominant for dominant integral $\lambda,\mu$, and a chamber meets a sphere in at most one point, so $\lambda+\rho=\mu+\rho$ and $\lambda=\mu$. $\square$

**Remark.** The injectivity fails if the whole Weyl orbit is admitted, the eigenvalue depending only on the orbit of $\lambda+\rho$; it is the choice of the dominant representative, that is of the highest weight, that makes the eigenvalue a label of the irreducible module.

### The Eigenspaces Are the Isotypic Components

**Theorem.** Let $V$ be a finite-dimensional completely reducible $\mathrm{G}$-module and let $V\cong\bigoplus_\nu V(\nu)^{\oplus m_\nu}$ be its decomposition into isotypic components. Then for each $\nu$

$$
V_{(\nu)}=\{\,v\in V : \Omega_\pi v=(\nu,\nu+2\rho)\,v\,\},
$$

the eigenspace of $\Omega_\pi$ for the eigenvalue $(\nu,\nu+2\rho)$; the eigenspaces of the Casimir operator are exactly the isotypic components.

**Proof.** On every copy of $V(\nu)$ the operator acts by the scalar $(\nu,\nu+2\rho)$, so $V_{(\nu)}$ lies in the eigenspace. Conversely the eigenvalues are distinct for distinct highest weights by the proposition, so an eigenvector with eigenvalue $(\nu,\nu+2\rho)$ lies in the sum of the copies of $V(\nu)$, and the two spaces coincide. $\square$

**Corollary.** The Casimir operator separates the isotypic components: it is a central operator whose characteristic polynomial has the distinct eigenvalues $(\nu,\nu+2\rho)$, and its eigenspace projections are the isotypic projections. In particular the multiplicity $m_\nu$ is the dimension of the corresponding eigenspace divided by $\dim V(\nu)$.

## The Invariant Tensor

### The Element and the Identity Operator

The Casimir element is the image of a canonical invariant tensor, and under the identification of $\mathrm{G}\otimes_K\mathrm{G}$ with $\operatorname{End}_K(\mathrm{G})$ that tensor is the identity.

**Definition.** The **invariant tensor** of the Killing form is

$$
\theta=\sum_{i=1}^{m}x_i\otimes x^i\in\mathrm{G}\otimes_K\mathrm{G}.
$$

It is independent of the basis, and it is invariant under the diagonal action of $\mathrm{G}$: $(\operatorname{ad}_x\otimes1+1\otimes\operatorname{ad}_x)\theta=0$.

**Proposition.** Under the linear isomorphism $\mathrm{G}\otimes_K\mathrm{G}\to\operatorname{End}_K(\mathrm{G})$ that sends $u\otimes v$ to the operator $z\mapsto\kappa(v,z)\,u$, the tensor $\theta$ corresponds to the identity:

$$
\theta\longmapsto \mathrm{id}_{\mathrm{G}}.
$$

**Proof.** The image of $z$ is $\sum_i\kappa(x^i,z)x_i$. Writing $z=\sum_j z_jx_j$, the dual-basis property gives $\kappa(x^i,z)=z_i$, so the image is $\sum_i z_ix_i=z$. $\square$

**Remark.** The proposition is the operator-theoretic content of the Casimir element: it is the invariant tensor that represents the identity, read in $U(\mathrm{G})$ instead of in $\mathrm{G}\otimes\mathrm{G}$. The same computation with the adjoint action in place of the pairing is the statement that the Casimir operator of the adjoint module is the identity, which is the next section.

## The Adjoint Module

**Theorem.** On the adjoint module $\mathrm{G}$ the Casimir operator is the identity,

$$
\Omega_{\operatorname{ad}}=\mathrm{id}_{\mathrm{G}},
\qquad
\Omega_{\operatorname{ad}}(x)=\sum_{i=1}^{m}[x_i,[x^i,x]]=x .
$$

**Proof.** The Casimir operator acts on the adjoint module by $\Omega_{\operatorname{ad}}(x)=\sum_i[x_i,[x^i,x]]$; by the invariance of $\kappa$ this equals the image of $x$ under the operator of the previous proposition, which is $x$. In the alternative form, the eigenvalue of the adjoint module is $(\theta,\theta+2\rho)$, with $\theta$ the highest root, and the normalisation of the Killing form makes this equal to $1$. $\square$

**Verified.** For $\mathrm{SL}(2,K)$ with the basis $e,h,f$ and the dual basis $f/4,e/4,h/8$ of the Killing form, the computation $\Omega_{\operatorname{ad}}(x)=\sum_i[x_i,[x^i,x]]$ gives $\Omega_{\operatorname{ad}}(e)=e$, $\Omega_{\operatorname{ad}}(h)=h$ and $\Omega_{\operatorname{ad}}(f)=f$ over $\mathbb{Q}$.

## Tensor Products

**Proposition (the mixed term).** Let $V$ and $W$ be $\mathrm{G}$-modules, and let $\Omega_V,\Omega_W$ be the Casimir operators. Then, on $V\otimes_KW$,

$$
\Omega_{V\otimes W}=\Omega_V\otimes\mathrm{id}_W+\mathrm{id}_V\otimes\Omega_W+2\sum_{i=1}^{m}\pi_V(x_i)\otimes\pi_W(x^i).
$$

**Proof.** This is the expansion of $\sum_i\pi_{V\otimes W}(x_i)\pi_{V\otimes W}(x^i)$ with $\pi_{V\otimes W}(x)=\pi_V(x)\otimes\mathrm{id}+\mathrm{id}\otimes\pi_W(x)$; the diagonal terms give the two Casimir operators, and the cross terms give twice the displayed mixed sum. $\square$

**Corollary.** On a tensor product of two irreducible modules the Casimir operator acts with the eigenvalues of the summands shifted by the mixed term, whose value is computed from the highest weights by the Littlewood–Richardson rule of *Representations of Lie Algebras*; for $\mathrm{SL}(2,K)$ the mixed term vanishes on the highest weight vector and the eigenvalue is the sum of the two eigenvalues.

## The Regular Representation

**Proposition.** In the regular representation, that is left multiplication on $U(\mathrm{G})$, the Casimir operator is left multiplication by $C$; it commutes with left multiplication by every element of $\mathrm{G}$, so it lies in $\operatorname{End}_{U(\mathrm{G})}(U(\mathrm{G}))$, and it acts on the centre of $U(\mathrm{G})$ by multiplication.

**Proof.** The regular representation sends $x$ to left multiplication by $x$, so $\Omega$ is left multiplication by $C$; centrality of $C$ in $U(\mathrm{G})$ is the commutation with every left multiplication. $\square$

**Remark.** The centre $Z(U(\mathrm{G}))$ of the enveloping algebra is a polynomial algebra over $K$ in $\operatorname{rank}\mathrm{G}$ generators, of which the Casimir element is the quadratic one; the higher Casimir operators are the higher generators, read as operators by the same construction. The theorem of Harish-Chandra and its proof belong to the representation theory of Part I and are named here only to locate the Casimir operator in the centre.

## Worked Case: $\mathrm{SL}(2,K)$

Let $\mathrm{SL}(2,K)$ have basis $e,h,f$ with $[e,f]=h$, $[h,e]=2e$, $[h,f]=-2f$, and Killing form $\kappa(e,f)=4$, $\kappa(h,h)=8$. The dual basis of $(e,h,f)$ is $(f/4,e/4,h/8)$, so

$$
C=\tfrac14(ef+fe)+\tfrac18h^2 .
$$

**The standard two-dimensional module.** With

$$
e=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
f=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
h=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
$$

one has $ef+fe=\mathrm{id}$ and $h^2=\mathrm{id}$, so $\Omega=\tfrac14\mathrm{id}+\tfrac18\mathrm{id}=\tfrac38\mathrm{id}$, in agreement with $\tfrac18n(n+2)$ at $n=1$.

**The adjoint module.** The computation above gives $\Omega_{\operatorname{ad}}=\mathrm{id}$, the eigenvalue $(\alpha,\alpha+2\rho)=1$ at the highest root $\alpha$ of $\mathrm{SL}(2,K)$.

**The general irreducible module.** On $V_n$ of highest weight $n\omega$ the operator is the scalar $\tfrac18n(n+2)$, a strictly increasing function of $n$; hence the Casimir operator alone separates the irreducible modules of $\mathrm{SL}(2,K)$.

## Summary

The **Casimir operator** of a representation $\pi$ of a semisimple Lie algebra is the operator $\Omega_\pi=\pi(C)=\sum_i\pi(x_i)\pi(x^i)$ attached to the Casimir element $C$ of $U(\mathrm{G})$; it is independent of the choice of basis, and it commutes with the action, $[\Omega_\pi,\pi(x)]=0$, so it is a $\mathrm{G}$-module endomorphism. It therefore preserves every submodule and descends to every quotient, and on an irreducible module it is a scalar, namely $(\lambda,\lambda+2\rho)$ for $V(\lambda)$. Because the eigenvalues of distinct highest weights are distinct, the eigenspaces of $\Omega_\pi$ on a completely reducible module are exactly the isotypic components, so the Casimir operator separates them and its eigenspace projections are the isotypic projections.

The Casimir element is the image of the invariant tensor $\theta=\sum_ix_i\otimes x^i$, which corresponds to the identity operator under the identification $\mathrm G\otimes\mathrm G\cong\operatorname{End}_K(\mathrm G)$; consistently, the Casimir operator of the adjoint module is the identity. On a tensor product it is the sum of the two Casimir operators and a mixed term, $\Omega_{V\otimes W}=\Omega_V\otimes1+1\otimes\Omega_W+2\sum_i\pi_V(x_i)\otimes\pi_W(x^i)$. In the regular representation it is left multiplication by $C$, hence an element of $\operatorname{End}_{U(\mathrm{G})}(U(\mathrm{G}))$, and it is the quadratic generator of the centre of $U(\mathrm{G})$. For $\mathrm{SL}(2,K)$ the dual basis of $(e,h,f)$ is $(f/4,e/4,h/8)$, the Casimir element is $\tfrac14(ef+fe)+\tfrac18h^2$, its operator is $\tfrac38\mathrm{id}$ on the two-dimensional module and $\mathrm{id}$ on the adjoint module, and on $V_n$ it is the strictly increasing scalar $\tfrac18n(n+2)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | algebraically closed base field of characteristic zero |
| $\mathrm{G}$ | finite-dimensional semisimple Lie algebra over $K$ |
| $\kappa$ | the Killing form |
| $x_i,x^i$ | a basis and its $\kappa$-dual basis |
| $C=\sum_ix_ix^i$ | the Casimir element of $U(\mathrm{G})$ |
| $\pi$ | a representation of $\mathrm{G}$ |
| $\Omega_\pi=\pi(C)$ | the Casimir operator of $\pi$ |
| $\operatorname{End}_{\mathrm{G}}(V)$ | the $\mathrm{G}$-module endomorphisms of $V$ |
| $V(\lambda)$, $(\lambda,\lambda+2\rho)$ | irreducible module and its Casimir eigenvalue |
| $\rho$ | the half-sum of the positive roots |
| $\theta=\sum_ix_i\otimes x^i$ | the invariant tensor of the Killing form |
| $\Omega_{\operatorname{ad}}=\mathrm{id}$ | the Casimir operator of the adjoint module |
| $V_{(\nu)}$ | the isotypic component of highest weight $\nu$ |

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Graduate Texts in Mathematics 9 (Springer, 1972), for the Casimir element and its eigenvalue.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 4–6 (Springer, 2002), for the invariant tensor of the Killing form and the centre of the enveloping algebra.
- Jacques Dixmier, *Enveloping Algebras*, Graduate Studies in Mathematics 11 (American Mathematical Society, 1996), for the centre of $U(\mathrm{G})$, the higher Casimir operators and the Harish-Chandra theorem.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the Casimir element as an element of the enveloping algebra and its role in complete reducibility.
- Jean-Pierre Serre, *Complex Semisimple Lie Algebras* (Springer, 2001), for the Casimir operator and the eigenvalue formula.
