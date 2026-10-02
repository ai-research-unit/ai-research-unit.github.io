
# __The Cartan Operator__

## Introduction

A **Cartan subalgebra** of a semisimple Lie algebra $\mathrm{G}$ is a maximal abelian subalgebra consisting of elements that act diagonalisably, and the **root space decomposition** is the simultaneous eigenspace decomposition of the operators $\operatorname{ad}_h=[h,-]$ for $h$ in it. This article studies those operators. For $h\in\mathrm{H}$ the **Cartan operator** is $\operatorname{ad}_h$, and the article treats the family $\{\operatorname{ad}_h\}_{h\in\mathrm{H}}$ as a commuting family of diagonalisable operators, the root decomposition as its joint eigenspace decomposition, the roots as the eigenvalues, and the Killing form as the invariant pairing under which the whole adjoint representation consists of skew adjoint operators. The Cartan subalgebra, the roots, the root system and the restriction of the Killing form to $\mathrm{H}$ are defined in *Root Systems and Classification*, and the Killing form, its invariance and its nondegeneracy are defined in *Structure of Lie Algebras*; nothing owned by those entries is re-derived.

The article belongs to the operator theory of the category: the object is the operator $\operatorname{ad}_h$ and the consequences of its diagonalisability, not the classification of the root systems, which is *Root Systems and Classification*, nor the construction of the highest weight modules, which is *Representations of Lie Algebras*. The base is an algebraically closed field $K$ of characteristic zero and $\mathrm{G}$ is finite-dimensional and semisimple over $K$; the Cartan subalgebra is written $\mathrm{H}$, the root system $\Phi\subseteq\mathrm{H}^*$, the root space of $\alpha$ is $\mathrm{G}_\alpha$, and the Killing form is $\kappa$.

## The Cartan Operators

### Definition

**Definition.** Let $\mathrm{H}$ be a Cartan subalgebra of $\mathrm{G}$. For $h\in\mathrm{H}$ the **Cartan operator** attached to $h$ is the adjoint operator

$$
\operatorname{ad}_h:\mathrm{G}\longrightarrow\mathrm{G},\qquad \operatorname{ad}_h(x)=[h,x].
$$

The family $\operatorname{ad}(\mathrm{H})=\{\operatorname{ad}_h : h\in\mathrm{H}\}$ is the image of $\mathrm{H}$ under the adjoint representation; it is an abelian subalgebra of $\operatorname{End}_K(\mathrm{G})$.

**Proposition.** The Cartan operators commute pairwise and are diagonalisable:

$$
[\operatorname{ad}_h,\operatorname{ad}_{h'}]=0,\qquad \operatorname{ad}_h\text{ is diagonalisable for every }h\in\mathrm{H}.
$$

**Proof.** The commutation is $[\operatorname{ad}_h,\operatorname{ad}_{h'}]=[h,h']=0$, the bracket being the adjoint representation of the abelian algebra $\mathrm{H}$; the diagonalisability is the defining property of a Cartan subalgebra of a semisimple algebra, stated in *Root Systems and Classification*. $\square$

### The Joint Eigenspace Decomposition

**Theorem (the root decomposition as an eigenspace decomposition).** The algebra decomposes as

$$
\mathrm{G}=\mathrm{H}\oplus\bigoplus_{\alpha\in\Phi}\mathrm{G}_\alpha,
\qquad
\mathrm{G}_\alpha=\{\,x : \operatorname{ad}_h(x)=\alpha(h)x\text{ for all }h\in\mathrm{H}\,\},
$$

and the joint eigenspaces of the family $\operatorname{ad}(\mathrm{H})$ are exactly the pieces $\mathrm{G}_\alpha$ and $\mathrm{H}=\mathrm{G}_0$.

**Proof.** Commuting diagonalisable operators are simultaneously diagonalisable, so $\mathrm{G}$ is the direct sum of the joint eigenspaces of the family; the definition of the root space is exactly the joint eigenspace for the eigenvalue function $\alpha$, and the zero eigenvalue function has the joint kernel $\mathrm{H}$ because a Cartan subalgebra equals its own normaliser. This is the root space decomposition of *Root Systems and Classification*. $\square$

**Corollary.** On each root space the Cartan operator acts by the scalar $\alpha(h)$:

$$
\operatorname{ad}_h|_{\mathrm{G}_\alpha}=\alpha(h)\,\mathrm{id},\qquad \operatorname{ad}_h|_{\mathrm H}=0 .
$$

**Remark.** The roots are the eigenvalues, read as functions of $h$. This is why the roots are elements of the dual $\mathrm{H}^*$: for each fixed operator $\operatorname{ad}_h$ the eigenvalue is a scalar, and the several operators assemble the eigenvalue into a linear functional on $\mathrm{H}$.

### The Action on the Root Spaces

**Proposition.** The root spaces satisfy $[\mathrm{G}_\alpha,\mathrm{G}_\beta]\subseteq\mathrm{G}_{\alpha+\beta}$ with $\mathrm{G}_\gamma=0$ for $\gamma\notin\Phi\cup\{0\}$, and for $x\in\mathrm{G}_\alpha$ the operator $\operatorname{ad}_x$ raises the root by $\alpha$:

$$
\operatorname{ad}_x(\mathrm{G}_\beta)\subseteq\mathrm{G}_{\alpha+\beta}.
$$

**Proof.** For $h\in\mathrm{H}$ and $y\in\mathrm{G}_\beta$, the Jacobi identity gives $[h,[x,y]]=[[h,x],y]+[x,[h,y]]=\alpha(h)[x,y]+\beta(h)[x,y]$, so $[x,y]\in\mathrm{G}_{\alpha+\beta}$. $\square$

**Corollary (the characteristic polynomial).** For $h\in\mathrm{H}$ the characteristic polynomial of the Cartan operator is

$$
\det(t\,\mathrm{id}-\operatorname{ad}_h)=t^{\dim\mathrm{H}}\prod_{\alpha\in\Phi}\bigl(t-\alpha(h)\bigr),
$$

a product of linear factors with multiplicities one, showing the diagonalisability directly.

## The Killing Form as an Invariant Pairing

### Invariance and Skew Adjunction

**Proposition.** The Killing form is invariant, $\kappa([x,y],z)=\kappa(x,[y,z])$, and with respect to it every adjoint operator is skew adjoint:

$$
\kappa(\operatorname{ad}_xy,z)=-\kappa(y,\operatorname{ad}_xz),\qquad\text{that is}\qquad \operatorname{ad}_x^{*}=-\operatorname{ad}_x .
$$

**Proof.** The invariance is from *Structure of Lie Algebras*; putting $y=x$ in the middle slot gives $\kappa([x,y],z)=\kappa(x,[y,z])$, that is $\kappa(\operatorname{ad}_xy,z)=-\kappa(y,\operatorname{ad}_xz)$, which is the defining relation of the adjoint with respect to the nondegenerate pairing $\kappa$. $\square$

**Corollary.** The adjoint representation is a homomorphism $\operatorname{ad}:\mathrm{G}\to\operatorname{End}_K(\mathrm{G})$ whose image lies in the Lie subalgebra of $\kappa$-skew operators; in particular each Cartan operator is $\kappa$-skew, and its nonzero eigenvalues come in opposite pairs.

**Proof.** The image of a homomorphism is a subalgebra, and the skew adjoint operators form a subalgebra because the adjoint operation reverses the commutator. For a skew operator the characteristic polynomial is even up to the kernel, so the nonzero eigenvalues occur in pairs $t,-t$. $\square$

### The Restriction to the Cartan Subalgebra

**Proposition.** The restriction of the Killing form to $\mathrm{H}$ is nondegenerate; the element $t_\alpha\in\mathrm{H}$ defined by $\kappa(t_\alpha,h)=\alpha(h)$ realises the root as a pairing, and the transported form $(\alpha,\beta)=\kappa(t_\alpha,t_\beta)$ on $\mathrm{H}^*$ is symmetric and nondegenerate, with the Cartan integers $2(\beta,\alpha)/(\alpha,\alpha)$ integral.

**Proof.** The nondegeneracy of $\kappa|_{\mathrm{H}}$ and the identity $\kappa(\mathrm{G}_\alpha,\mathrm{G}_\beta)=0$ unless $\alpha+\beta=0$ are from *Root Systems and Classification*, together with the integrality of the Cartan integers. $\square$

**Remark.** The pairing is the operator-theoretic bridge between the Cartan operators and the root system: the eigenvalue $\alpha(h)$ is $\kappa(t_\alpha,h)$, so the operator $\operatorname{ad}_h$ has eigenvalue $\kappa(t_\alpha,h)$ on $\mathrm{G}_\alpha$, and the Cartan operator attached to $t_\alpha$ has the eigenvalue $(\alpha,\alpha)$ on $\mathrm{G}_\alpha$ and $(\alpha,\beta)$ on $\mathrm{G}_\beta$. The form $(\cdot,\cdot)$ transported to the span of the roots is symmetric and nondegenerate, and the further structure that it carries on the real span of the roots is named in Part II and is not used here.

## The Cartan Operator and the Casimir Operator

**Proposition.** Let $(h_1,\dots,h_r)$ be a basis of $\mathrm{H}$ and $(h^1,\dots,h^r)$ its dual basis with respect to $\kappa|_{\mathrm{H}}$. Then the operator $\sum_i\operatorname{ad}_{h_i}\operatorname{ad}_{h^i}$ acts on $\mathrm{H}$ by zero and on $\mathrm{G}_\alpha$ by the scalar $\sum_i\alpha(h_i)\alpha(h^i)=(\alpha,\alpha)$.

**Proof.** Each factor acts on $\mathrm{G}_\alpha$ by the scalar $\alpha(h_i)$ and $\alpha(h^i)$ respectively; the sum is $\sum_i\alpha(h_i)\alpha(h^i)$, which is the pairing of $\alpha$ with itself by the definition of the dual basis. On $\mathrm{H}$ both factors are zero. $\square$

**Remark.** The proposition is the Cartan part of the Casimir operator of *The Casimir Operator*: the full Casimir operator is the sum of this Cartan part and the contributions of the root spaces, and the eigenvalue on the adjoint module is one by the identity $\Omega_{\operatorname{ad}}=\mathrm{id}$ proved there. The Cartan part alone has the eigenvalues $(\alpha,\alpha)$ on the root spaces and is the part that a highest weight calculation reads off first.

## Worked Cases

### The Lie Algebra $\mathrm{SL}(2,K)$

Let $\mathrm{SL}(2,K)$ have basis $e,h,f$ with $[e,f]=h$, $[h,e]=2e$, $[h,f]=-2f$; the Cartan subalgebra is $\mathrm{H}=K h$, and the roots are $\pm\alpha$ with $\alpha(h)=2$. The Cartan operator is

$$
\operatorname{ad}_h=\begin{pmatrix}2&0&0\\0&0&0\\0&0&-2\end{pmatrix}
$$

in the basis $(e,h,f)$, so its eigenvalues are $2,0,-2$ and its characteristic polynomial is $-t(t-2)(t+2)$; the nonzero eigenvalues are opposite, as the skew adjointness requires. The Cartan part of the Casimir operator acts on $\mathrm{G}_\alpha=Ke$ and $\mathrm{G}_{-\alpha}=Kf$ by $(\alpha,\alpha)=\tfrac12$ with the Killing normalisation $(\omega,\omega)=\tfrac18$ and $\alpha=2\omega$, and the full Casimir operator is the identity on the adjoint module.

### The Root System $A_2$

Let $\mathrm{G}=\mathrm{SL}(3,K)$ with $\mathrm{H}$ the diagonal matrices of trace zero and roots $\alpha_1,\alpha_2;\alpha_1+\alpha_2$, the positive roots, and their negatives. The Cartan operators act by the scalars $\alpha(h)$; the characteristic polynomial of a generic $\operatorname{ad}_h$ has the six nonzero roots $\pm\alpha_1(h),\pm\alpha_2(h),\pm(\alpha_1+\alpha_2)(h)$ and the zero root of multiplicity two, and the Cartan matrix

$$
\begin{pmatrix}2&-1\\-1&2\end{pmatrix}
$$

records the pairings $2(\alpha_i,\alpha_j)/(\alpha_j,\alpha_j)$. The root decomposition has $\dim\mathrm{G}_\alpha=1$ for each of the six roots, so the algebra is $\mathrm{H}$ together with six one-dimensional spaces.

**Verified.** For $\mathrm{SL}(2,K)$ the matrix of $\operatorname{ad}_h$ in the basis $(e,h,f)$ has eigenvalues $2,0,-2$ over $\mathbb{Q}$; for $A_2$ the six roots are the six nonzero functionals, checked against the structure constants of $\mathrm{SL}(3,K)$.

## Summary

The **Cartan operators** are the adjoint operators $\operatorname{ad}_h$ for $h$ in a Cartan subalgebra $\mathrm{H}$; they commute pairwise and are diagonalisable, so they admit a joint eigenspace decomposition, and that decomposition is the root space decomposition $\mathrm{G}=\mathrm{H}\oplus\bigoplus_{\alpha\in\Phi}\mathrm{G}_\alpha$, with $\mathrm{G}_\alpha$ the joint eigenspace of the eigenvalue function $\alpha$. On $\mathrm{G}_\alpha$ the Cartan operator acts by the scalar $\alpha(h)$, so the roots are the eigenvalues read as functionals on $\mathrm{H}$, and the characteristic polynomial of $\operatorname{ad}_h$ is $t^{\dim\mathrm{H}}\prod_\alpha(t-\alpha(h))$. The bracket satisfies $[\mathrm{G}_\alpha,\mathrm{G}_\beta]\subseteq\mathrm{G}_{\alpha+\beta}$, so an operator $\operatorname{ad}_x$ with $x\in\mathrm{G}_\alpha$ raises the root by $\alpha$.

The Killing form is invariant, and every adjoint operator is skew adjoint with respect to it, so the adjoint representation lands in the skew adjoint operators and the nonzero eigenvalues of each Cartan operator occur in opposite pairs. The restriction of the Killing form to $\mathrm{H}$ is nondegenerate and transports to the form $(\alpha,\beta)$ on $\mathrm{H}^*$, with the Cartan integers $2(\beta,\alpha)/(\alpha,\alpha)$ integral. The Cartan part $\sum_i\operatorname{ad}_{h_i}\operatorname{ad}_{h^i}$ of the Casimir operator acts on $\mathrm{G}_\alpha$ by $(\alpha,\alpha)$ and annihilates $\mathrm{H}$, and the full Casimir operator is the identity on the adjoint module. For $\mathrm{SL}(2,K)$ the Cartan operator has eigenvalues $2,0,-2$; for $A_2$ it has the six nonzero roots and the Cartan matrix $[[2,-1],[-1,2]]$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | algebraically closed base field of characteristic zero |
| $\mathrm{G}$ | finite-dimensional semisimple Lie algebra over $K$ |
| $\mathrm{H}$ | a Cartan subalgebra, abelian and self-normalising |
| $\operatorname{ad}_h$ | the Cartan operator attached to $h\in\mathrm{H}$ |
| $\Phi\subseteq\mathrm{H}^*$ | the root system |
| $\mathrm{G}_\alpha$ | the root space of $\alpha$, a joint eigenspace |
| $\kappa$ | the Killing form, invariant and nondegenerate |
| $t_\alpha$ | the element of $\mathrm{H}$ with $\kappa(t_\alpha,h)=\alpha(h)$ |
| $(\alpha,\beta)=\kappa(t_\alpha,t_\beta)$ | the transported form on $\mathrm{H}^*$ |
| $\operatorname{ad}(\mathrm{G})\subseteq\mathfrak{so}(\mathrm{G},\kappa)$ | the adjoint operators are $\kappa$-skew |

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Graduate Texts in Mathematics 9 (Springer, 1972), for Cartan subalgebras, the root space decomposition and the Killing form.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 4–6 (Springer, 2002), for the simultaneous diagonalisation of the Cartan operators and the Cartan integers.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the adjoint operators, their eigen-decomposition and the invariant form.
- Jean-Pierre Serre, *Complex Semisimple Lie Algebras* (Springer, 2001), for the root space decomposition and the integrality of the Cartan integers.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces*, Graduate Studies in Mathematics 34 (American Mathematical Society, 2001), for the Cartan decomposition and the skew adjointness that reappears in the symmetric-space theory of Part II.
