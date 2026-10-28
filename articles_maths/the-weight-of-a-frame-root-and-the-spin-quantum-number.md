# __The Weight of a Frame Root and the Spin Quantum Number__

## Introduction

The words **generator**, **carrier**, **weight** and **spin** are often used before they are defined. This article defines them in the order in which they depend on one another, and then computes them for the frame that one idempotent supplies.

An idempotent $e$ of a unital algebra $A$ gives the **frame root** $h=2e-1_A$. The root is an element of the algebra. A **carrier** is a vector space together with an action of the algebra, either by left multiplication or by the commutator. The **generator on the carrier** is the operator by which $h$ acts. A **weight** is an eigenvalue of that operator, and the **weight string** is the list of eigenvalues with their multiplicities. The **highest weight** is the largest of them once an order is chosen. The **spin** is half the highest weight, in the normalisation in which the highest weight of the defining carrier is $2j$.

Three results organise the article. First, the Peirce corners make the weights of $h$ explicit: left multiplication has weight $+1$ on the corners with left index $+$ and $-1$ on those with left index $-$, right multiplication has weight $+1$ on those with right index $+$ and $-1$ on those with right index $-$, and the commutator has the difference. Second, a weight string of the form $\lambda,\lambda-2,\dots,-\lambda$ is exactly a finite-dimensional representation of an $\mathfrak{sl}_2$ triple, and then the spin is $j=\lambda/2$. Third, one idempotent supplies the root but not the triple: the Peirce root of a primitive idempotent of $M_N(k)$ closes to an $\mathfrak{sl}_2$ exactly when $N=2$, which is the algebraic reason the biquaternion carries a canonical spin one-half.

**Setting.** Throughout, $k$ is a field of characteristic zero, $A$ is a finite-dimensional unital associative $k$-algebra with $1_A\neq0$, $e\in A$ is an idempotent, $f=1_A-e$, and $h=2e-1_A$. The corners are $A_{st}=e_sAe_t$ with $e_+=e$, $e_-=f$. The Peirce decomposition and the companion count are *Peirce Coordinates and Companion Nilpotents*; the spinor carrier is *Spinors as Peirce Coordinates*; the highest-weight theory of Lie algebras is *Representations of Lie Algebras*; and the normalisation "highest weight $2j$, spin $j$" is that of *Biquaternion Rotations and Lorentz Transformations*.

## Generator and Carrier

**Definition.** The **frame root** of $e$ is

$$
h=2e-1_A=e-f .
$$

It satisfies $h^2=1_A$, and in $M_N(k)$ its trace is $\operatorname{tr}h=2\operatorname{tr}e-N$.

**Definition.** A **carrier** is a pair $(W,\rho)$ of a finite-dimensional $k$-vector space $W$ and a linear map $\rho$ on $W$ that is either

- an **associative action**, an algebra homomorphism $\rho:A\to\operatorname{End}_k(W)$ with $\rho(ab)=\rho(a)\rho(b)$, or
- a **Lie action**, a Lie algebra homomorphism $\rho:(A,[\,,\,])\to\operatorname{End}_k(W)$ with $\rho([a,b])=[\rho(a),\rho(b)]$.

The **generator on the carrier** is the operator $\rho(h)$. The space alone is not the carrier; the action is part of the data.

**Remark.** The two kinds are not interchangeable. Left multiplication is associative; the commutator is not, because $\operatorname{ad}_{ab}\neq\operatorname{ad}_a\operatorname{ad}_b$ in general. This is why the same element $h$ can have weights $+1,-1$ on a Peirce carrier and $+2,0,-2$ on the traceless part: the actions are different, not the element.

## Weight

**Definition.** Let $(W,\rho)$ be a carrier and $T=\rho(h)$. A **weight** of $h$ on $W$ is an eigenvalue $\lambda\in k$ of $T$; the **weight space** is $W_\lambda=\ker(T-\lambda)$; the **weight string** is the multiset of eigenvalues, counted with the dimensions of their weight spaces. A **highest weight** is a weight that is maximal for a chosen order on $k$; when the weights are real, the order is the usual one.

**Definition.** Let $(u,v,h)$ be a triple of elements of $A$ with

$$
[h,u]=2u,\qquad [h,v]=-2v,\qquad [u,v]=h .
$$

It is an **$\mathfrak{sl}_2$ triple**, and a carrier on which the three act is an **$\mathfrak{sl}_2$ carrier**. A vector $w\in W$ is a **highest weight vector** of weight $\lambda$ when $\rho(h)w=\lambda w$ and $\rho(u)w=0$.

**Remark (the word "weight" has two uses in the corpus).** The Peirce weight is the eigenvalue of a frame root. The Lorentz weight $(j_1,j_2)$ labels a finite-dimensional representation of the Lorentz group. The two agree on the rotation subgroup and they are not the same object; this article uses the first sense and writes the second only in the examples of the Lorentz layer.

## The Peirce Weights

**Proposition.** On the corner $A_{st}$, the left multiplication $L_h$ has weight $s$, the right multiplication $R_h$ has weight $t$, and the inner derivation $\operatorname{ad}_h=L_h-R_h$ has weight $s-t$. In tabular form:

| corner | $L_h$ | $R_h$ | $\operatorname{ad}_h$ |
|---|---|---|---|
| $A_{++}$ | $+1$ | $+1$ | $0$ |
| $A_{+-}$ | $+1$ | $-1$ | $+2$ |
| $A_{-+}$ | $-1$ | $+1$ | $-2$ |
| $A_{--}$ | $-1$ | $-1$ | $0$ |

*Proof.* For $x\in A_{st}$, $hx=(2e-1_A)x=2\delta_{s+}x-x$, which is $+x$ for $s=+$ and $-x$ for $s=-$; similarly $xh=2\delta_{t+}x-x$. The difference is $s-t$.

**Corollary.** On the Peirce carrier $C(e)=Ae=A_{++}\oplus A_{-+}$, the left multiplication by $h$ has weight $+1$ on the diagonal part and $-1$ on the companion part. The commutator by $h$ has weight $+2$ on $A_{+-}$, $0$ on the diagonal corners, and $-2$ on $A_{-+}$; on the traceless part of a matrix algebra this gives the weights $+2,0,-2$.

**Remark (the shift by the right action).** The identity $L_h=\operatorname{ad}_h+R_h$ explains the factor two between the two carriers. On $A_{st}$ the right action contributes $t$, so the left weight $s$ is the commutator weight $s-t$ plus the right weight $t$. On the carrier $A_{++}\oplus A_{-+}$ the right weight is $+1$ on both summands, and the left weights $+1,-1$ become the commutator weights $0,-2$. On the traceless part the diagonal weights are $0$ and the mixed weights are $\pm2$. The factor two is a change of action, not a rescaling of the root.

## When the Root Closes to an $\mathfrak{sl}_2$

**Proposition.** Let $u\in A_{+-}$ and $v\in A_{-+}$ be nonzero. Then $[h,u]=2u$ and $[h,v]=-2v$ automatically, and the only further condition for $(u,v,h)$ to be an $\mathfrak{sl}_2$ triple is $[u,v]=h$. Equivalently, $h\in[A_{+-},A_{-+}]$.

*Proof.* The corner weights of $\operatorname{ad}_h$ are $+2$ on $A_{+-}$ and $-2$ on $A_{-+}$ by the table. The bracket $[A_{+-},A_{-+}]$ lies in $A_{++}$ by the multiplication table, and the remaining relation is $[u,v]=h$.

**Proposition (the matrix algebra).** Let $A=M_N(k)$ and let $e$ be a primitive idempotent. Then $h=2e-1_A$ closes to an $\mathfrak{sl}_2$ triple exactly when $N=2$.

*Proof.* The trace of a commutator is zero, so a necessary condition is $\operatorname{tr}h=0$. For a primitive idempotent $\operatorname{tr}e=1$, hence $\operatorname{tr}h=2-N$, which vanishes only for $N=2$. For $N=2$, with $e=E_{11}$, take $u=E_{12}$ and $v=E_{21}$: then $[u,v]=E_{11}-E_{22}=h$, and the other two relations hold by the table.

**Example (the biquaternion).** In $\mathbb{B}$ with the standard frame $e=\tilde\Pi_+$, the root is the pure element $h=\vec\Xi=\tilde\Pi_+-\tilde\Pi_-=i\vec e_z$, and

$$
u=\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y),\qquad
v=\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)
$$

satisfy $[u,v]=h$. The triple is $(u,v,h)$, and the two nilpotents are the two companion nilpotents of the frame.

**Example (the failure in $M_3$).** With $e=E_{11}$, $h=2E_{11}-1_A$ has trace $-1$, while every commutator is traceless; so $h$ is not a commutator and no triple exists. The carrier is still irreducible, of dimension three, but the Peirce root does not put a spin on it. The principal $\mathfrak{sl}_2$ of $M_3$ does, with a different root $h'=\operatorname{diag}(2,0,-2)$, and gives spin $1$ on the same carrier. The spin depends on the triple, not on the idempotent alone.

## The Highest Weight and the Spin

**Theorem.** Let $(u,v,h)$ be an $\mathfrak{sl}_2$ triple and let $W$ be a finite-dimensional carrier generated by a highest weight vector $w$ of weight $\lambda$, with $\rho(u)w=0$. Then $\lambda$ is a nonnegative integer, the weights are

$$
\lambda,\ \lambda-2,\ \dots,\ -\lambda,
$$

each with multiplicity one, $\dim W=\lambda+1$, and the **spin** is

$$
j=\frac{\lambda}{2}=\frac{\lambda_{\max}-\lambda_{\min}}{4}.
$$

*Proof.* Put $w_k=\rho(v)^k w$. The relation $[h,v]=-2v$ gives $\rho(h)w_k=(\lambda-2k)w_k$, and the relation $[u,v]=h$ gives $\rho(u)w_k=k(\lambda-k+1)w_{k-1}$. The vectors $w_0,\dots,w_k$ are independent while they are nonzero, because they have distinct weights. Finite-dimensionality forces the string to terminate: if $w_{\lambda+1}\neq0$, then $\rho(u)w_{\lambda+1}=0$ and $w_{\lambda+1}$ has weight $-\lambda-2$, and the same construction would produce the infinite strictly decreasing string $-\lambda-2,-\lambda-4,\dots$. Hence $w_{\lambda+1}=0$, and then $w_0,\dots,w_\lambda$ span $W$ and are independent. So the weights are as stated and $\dim W=\lambda+1$. The equality $\lambda/2=(\lambda_{\max}-\lambda_{\min})/4$ is $\lambda_{\min}=-\lambda$. The normalisation $\lambda=2j$ is the one of *Biquaternion Rotations and Lorentz Transformations*, where the irreducible module $V_j$ has highest weight $2j$ and dimension $2j+1$.

**Remark (what the theorem does not say).** The theorem applies to a highest-weight carrier of an $\mathfrak{sl}_2$. It does not apply to a carrier whose weights are $\lambda,-\lambda,-\lambda,\dots$ with a repeated lowest weight, because such a string is not the weight string of an irreducible $\mathfrak{sl}_2$-module. The Peirce carrier of $M_3$ with $e=E_{11}$ is of this kind: its weights are $+1,-1,-1$, and the number $\frac12\lambda_{\max}=\frac12$ is not a spin. The repeated weight is the signal that the Peirce root is not a Cartan element of an $\mathfrak{sl}_2$ on that carrier.

## Two Carriers of the Same Root

In the biquaternion the root $h=\vec\Xi$ acts on two carriers, and they are the two spin cases of the corpus.

**The Peirce carrier.** On $C(\tilde\Pi_+)=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_y$, the left multiplication $L_h$ has weights $+1$ and $-1$. The triple is $(u,v,h)=(\vec\Upsilon_x,\vec\Upsilon_y,\vec\Xi)$, the highest weight is $\lambda=1$, and

$$
j=\frac12 .
$$

The two coordinates are the two components of the spinor.

**The traceless part.** On $V=\operatorname{span}_{\mathbb{C}}\{\vec\Upsilon_x,\vec\Xi,\vec\Upsilon_y\}$, the commutator $\operatorname{ad}_h$ has weights $+2,0,-2$. The highest weight is $\lambda=2$, and

$$
j=1 .
$$

The three coordinates are the three components of a complex four-vector's vector part.

**The rotor.** Put $J_3=\frac12h$. On the carrier $J_3$ has weights $\pm\frac12$; on the traceless part it has weights $0,\pm1$. The unit element

$$
\tilde u(\theta)=\exp\!\left(\frac{\theta}{2}\vec e_z\right)
=\exp\!\left(-\frac{i\theta}{2}h\right)
=\exp\!\left(-i\theta J_3\right)
$$

acts by left multiplication on the carrier and by the commutator on the traceless part. In the standard matrix model it is $\operatorname{diag}(e^{-i\theta/2},e^{i\theta/2})$ on the carrier, and it has eigenvalues $1,e^{-i\theta},e^{i\theta}$ on $V$. The exponent is $\theta/2$ in the first case and $\theta$ in the second. The half-angle is the exponential coordinate of the weight under $J_3$; the full angle is the exponential coordinate of the weight on the traceless part. They are one root and two actions, not two definitions.

**Table of the two carriers.**

| carrier | action | weights of $h$ | highest weight | $j$ |
|---|---|---|---|---|
| $C(\tilde\Pi_+)$ | $L_h$ | $+1,-1$ | $1$ | $\tfrac12$ |
| $C(\tilde\Pi_-)$ | $L_h$ | $+1,-1$ | $1$ | $\tfrac12$ |
| traceless part $V$ | $\operatorname{ad}_h$ | $+2,0,-2$ | $2$ | $1$ |
| centre $\mathbb{C}_{\mathbb{B}}$ | trivial | $0$ | $0$ | $0$ |

## The Hermitian Real Form

**Definition.** Let $A$ carry an involution $*$. The frame root is **Hermitian** when $h^*=h$. In the biquaternion with the star, $h=\vec\Xi=i\vec u$ with $\vec u$ a real unit vector, and $J_3=\frac12h$ is the Hermitian spin operator $\tilde S_{\vec u}=\frac{\hbar}{2}i\vec u$ with $\hbar=1$.

**Proposition.** If $h$ is Hermitian, its weights on a unitary carrier are real and the weight spaces are orthogonal. If $h$ is not Hermitian, the weights are still defined algebraically, but $J_3$ is not an observable.

*Proof.* A Hermitian operator on a finite-dimensional space with a positive definite Hermitian form has real eigenvalues and orthogonal eigenspaces. The algebraic weights are the roots of the characteristic polynomial and do not require the form; the physical interpretation does.

**Remark.** The algebra supplies the weights for every idempotent; the real form selects the Hermitian family, which is the one the physics uses. The biquaternion's material sector $\mathbb{M}_-$ and informational sector $\mathbb{M}_+$ are real forms of the same complex algebra; the spin operator belongs to $\mathbb{M}_+$ when $h$ is Hermitian.

## Summary

The frame root is $h=2e-1_A$. A carrier is a space with an associative or a Lie action; the generator on the carrier is $\rho(h)$; a weight is an eigenvalue of $\rho(h)$; the weight string is the list with multiplicities; the highest weight is the largest for a chosen order; and the spin is $j=\lambda_{\max}/2=(\lambda_{\max}-\lambda_{\min})/4$ when the string is that of an irreducible $\mathfrak{sl}_2$-module.

The Peirce corners give the weights explicitly: $L_h$ has weight $s$ on $A_{st}$, $R_h$ has weight $t$, and $\operatorname{ad}_h$ has weight $s-t$. On the Peirce carrier the weights are $+1,-1$, and on the traceless part they are $+2,0,-2$. The root closes to an $\mathfrak{sl}_2$ when $h\in[A_{+-},A_{-+}]$; for a primitive idempotent of $M_N(k)$ this happens exactly when $N=2$. The biquaternion is that case: the carrier has weight $1$, spin $\tfrac12$, and the traceless part has weight $2$, spin $1$. Larger matrix algebras have irreducible carriers but no Peirce triple, and their spin depends on an extra choice of $\mathfrak{sl}_2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | A finite-dimensional unital associative $k$-algebra |
| $e$ | An idempotent, $f=1_A-e$ |
| $h=2e-1_A$ | The frame root |
| $(W,\rho)$ | A carrier: a space with an associative or a Lie action |
| $\rho(h)$ | The generator on the carrier |
| $\lambda$, $W_\lambda$ | A weight and its weight space |
| $\lambda_{\max},\lambda_{\min}$ | The highest and lowest weights for a chosen order |
| $(u,v,h)$ | An $\mathfrak{sl}_2$ triple, $[h,u]=2u$, $[h,v]=-2v$, $[u,v]=h$ |
| $j$ | The spin, $j=\lambda/2$ on a highest-weight carrier |
| $J_3=\frac12h$ | The Hermitian spin generator when $h$ is Hermitian |

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the $\mathfrak{sl}_2$ weight strings and the highest-weight theorem.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the highest weights and the symmetric powers.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce corners and their left and right weights.
- The corpus articles *Representations of Lie Algebras*, for the highest-weight theory, *Peirce Coordinates and Companion Nilpotents*, for the corner weights, and *Spinors as Peirce Coordinates*, for the carrier on which the weights are read.
