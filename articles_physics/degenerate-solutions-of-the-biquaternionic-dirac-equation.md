# __Degenerate Solutions of the Biquaternionic Dirac Equation__

## Introduction

*The Polar Form of the Dirac Equation in Biquaternionic Form* reads the Dirac equation through the polar word of the field, and that word exists exactly on the $N$-regular elements. Its domain is the open set $N\neq0$ and its boundary is the cone $N=0$. This article takes the boundary as its subject. It asks what a solution of the Dirac equation looks like when the norm of the field vanishes at a point, and what the equation has to say about such a field.

Three results organise the answer, and each corrects a guess that comes naturally.

The first is that the equation does not exclude a degenerate field. For a massive plane wave the polarization biquaternion is free: every element of $\mathbb{B}$ is the polarization of exactly one solution, and the pair fixes only the split of that element into its two components. Degeneracy is a condition on the field alone, one complex equation on four complex coefficients, and the equation neither imposes it nor forbids it.

The second is that the degenerate set is the cone, and the cone carries exactly two non-zero sectors, $\Sigma_{01}$ and $\Sigma_{00}$. Each has a component form, a worked example and a reading. The readings are the ones the polar companion gives from the other side: $\Sigma_{01}$ is a ray that keeps a direction and a weight, and $\Sigma_{00}$ is a null direction that keeps neither.

The third is that at $k_m=0$ the two lines of the pair decouple, and every non-zero one-sided solution is degenerate. Degeneracy is then not a codimension-two accident but the generic case, which is why a massless field is written as a sum of two one-sided fields: the sum is generically a unit, and the interference of the two parts is what carries the norm.

**A warning about letters.** Three different objects are called $L$ and $R$ in the corpus, and one of them cannot be substituted into the pair. The next section separates the three. The separation is not pedantry: the substitution that looks most natural makes both lines of the pair vanish, so a reader who takes it writes an article about the zero field.

## The Equation and the Field

The equation is the chiral pair of *The Dirac Equation in Biquaternionic Form*,

$$
\boxed{\;
\tilde\nabla_\Phi\tilde\Xi_{\mathrm{sp},R}=k_m\,\tilde\Xi_{\mathrm{sp},L},
\qquad
(\tilde\nabla^{\natural})_\Phi\tilde\Xi_{\mathrm{sp},L}=k_m\,\tilde\Xi_{\mathrm{sp},R},
\;}
$$

with $k_m=mc/\hbar$ the mass wave number, that is the reciprocal reduced Compton length. The field is one element $\tilde\Xi_{\mathrm{sp}}=\tilde\Xi_{\mathrm{sp},L}+\tilde\Xi_{\mathrm{sp},R}$ of $\mathbb{B}$. The gradient differentiates with respect to the coordinates $R_\mu$ and is an element of the algebra that multiplies on the left; the mass is a central coefficient. No column, no anticommuting array, no separate state space and no idempotent enters the statement.

At $k_m=0$ the pair decouples into two one-sided equations,

$$
\tilde\nabla_\Phi\tilde\Xi_{\mathrm{sp},R}=0,
\qquad
(\tilde\nabla^{\natural})_\Phi\tilde\Xi_{\mathrm{sp},L}=0 .
$$

**Definition.** A solution is **degenerate** at a point when $N\bigl(\tilde\Xi_{\mathrm{sp}}\bigr)=0$ there. It is degenerate when the condition holds at every point of its domain.

The norm here is the quaternionic norm $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$, the corpus's $\langle\cdot\rangle_{\natural}$, which is the determinant of the matrix model and is multiplicative (*The Meaning of N Regularity and Degeneracy*, §*The Norm and Its Identity*). Its value is $\langle\tilde Q\rangle_{\natural}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$, and its zero set is the cone $\mathcal N$, of real dimension six inside the algebra's eight, singular at the apex and smooth elsewhere.

Two facts about the cone are used throughout, and both are proved in the companion. On the cone the scalar part decides the spectral type: with $\tilde Q=Q_te_t+\vec Q$ and $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$, the identity $N=Q_t^{2}+B^{2}$ makes $Q_t\neq0$ equivalent to $B^{2}\neq0$. And on the cone the non-zero elements fall into the two sectors

$$
\Sigma_{01}=\{\tilde Q^{2}=\lambda\tilde Q,\ \lambda\neq0\},
\qquad
\Sigma_{00}=\{\tilde Q^{2}=0,\ \tilde Q\neq0\},
$$

which are the idempotent multiples and the nilpotents of index two. The scalar $\lambda$ is the non-zero eigenvalue, and $\lambda=2Q_t$; the companion writes it $c$, and this article writes $\lambda$ so that the letter $c$ stays the speed of light.

## Three Things Called L and R

### The Operator Label

The first object is a **membership in the operator algebra**. Left multiplication by an element is a linear map $L(\tilde A)\colon\tilde X\mapsto\tilde A\tilde X$, and the set of all of them is the image $L(\mathbb{B})\subseteq\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. The right multipliers form the image $R(\mathbb{B})$ in the same way. An operator is of the left slot, of the right slot, of both, or of neither, and the four cases are read from the multiplication alone, with no element chosen (*Operator Chirality on the Biquaternion Algebra*, §*What Operator Chirality Is Not*).

This label is not used below. It is named here only so that it is not confused with the other two.

### The Decomposition by a Declared Unit

The second object is a **split of an element**, and it needs one choice. Declare a traceless element $u$ with $u^{2}=-e_t$. Then $R_u^{2}=-\mathrm{id}$, so $R_u$ has eigenvalues $\pm i$, and every element splits as

$$
\tilde X=\tilde X_L+\tilde X_R,
\qquad
R_u\tilde X_L=i\tilde X_L,
\qquad
R_u\tilde X_R=-i\tilde X_R,
$$

with each part of complex dimension two. Written out,

$$
\tilde X_L=\tfrac12\bigl(\tilde X-i\tilde Xu\bigr),
\qquad
\tilde X_R=\tfrac12\bigl(\tilde X+i\tilde Xu\bigr).
$$

The idempotent $\tfrac12(e_t+iu)$ is derived from this split and is not its definition. The unit $u$ is a declared frame choice: choose another $u$ and the two halves change, so the split is a reading of the field and not a property of it.

At $u=\vec e_z$ this split is the corpus's **value test**: $\tilde X\vec e_z=-i\tilde X$ is the value $L$ and $\tilde X\vec e_z=+i\tilde X$ is the value $R$. The two units $\pm\vec e_z$ give the same split with the two letters exchanged, so the value test is the split of this section at one declared unit.

### The Pair's Two Components

The third object is the pair's own letters. They name **two components related by a central coefficient**, and no element is declared to state them. The definition is the equation: $\tilde\Xi_{\mathrm{sp},R}$ is the component the gradient acts on in the first line and $\tilde\Xi_{\mathrm{sp},L}$ is the component the conjugate gradient acts on in the second, and $k_m$ is the coefficient of the exchange. The parent article argues this at length in §*The Subscript and the Two Parts*, and the argument is one line: a left multiplier keeps the value, since $(\tilde A\tilde X)\vec e_z=\tilde A(\tilde X\vec e_z)$, so no term of the pair moves a value across.

### The Theorem That Separates Them

The third object cannot be the second, and the reason is one associativity step.

*Theorem.* Let $u$ be a traceless element with $u^{2}=-e_t$ and let $\tilde\Xi_{\mathrm{sp},L}$ and $\tilde\Xi_{\mathrm{sp},R}$ be definite-value parts under it, that is $R_u\tilde\Xi_{\mathrm{sp},L}=i\tilde\Xi_{\mathrm{sp},L}$ and $R_u\tilde\Xi_{\mathrm{sp},R}=-i\tilde\Xi_{\mathrm{sp},R}$. If $k_m\neq0$, then the pair holds only for $\tilde\Xi_{\mathrm{sp},L}=\tilde\Xi_{\mathrm{sp},R}=0$.

*Proof.* Left multiplication keeps a value, because a left multiplier acts before the right multiplier that tests the value: if $\tilde Xu=-i\tilde X$ then $(\tilde A\tilde X)u=\tilde A(\tilde Xu)=-i\tilde A\tilde X$. The gradient is an element and multiplies on the left, so $\tilde\nabla_\Phi\tilde\Xi_{\mathrm{sp},R}$ carries the value $-i$ wherever $\tilde\Xi_{\mathrm{sp},R}$ does. The right side of the first line is $k_m\tilde\Xi_{\mathrm{sp},L}$, of value $+i$, and the central coefficient does not move a value. Two definite-value elements of opposite value are equal only if both vanish, so the first line forces both sides to zero and then forces both components to vanish. The same argument applies to the second line, and it holds at each point of the field's domain, with no plane-wave assumption.

**Why the proof is short.** The only fact used is that multiplication on the left cannot change a value. A reader who takes the pair's letters to be definite values has already assumed that the operator acting on a component acts on the left, and the argument then applies to every field and every point, with no further hypothesis. The corpus's letters are not definite values, and that is the whole difference: the two components are related by a central coefficient, not by a sign of a right multiplier.

**The corollary is the useful form.** Inserting the decomposition of §*The Decomposition by a Declared Unit* into the pair returns the zero field, for every $u$ and for either assignment of signs. So the $u$-split is not a parametrisation of the pair's two components; it is a parametrisation of two objects the pair annihilates. The corpus's own proposition gives the other half of the reason: a definite-value element is a zero divisor and has $N=0$, so the two halves would be degenerate at every point of every solution (*The Polar Form of the Dirac Equation*, §*One Element, Two Parts*).

**A check.** The momentum-space system with the $u$-split substituted becomes four complex equations on the single unknown $\tilde\Xi_{\mathrm{sp},0}$, and its solution space has complex dimension zero. Five candidate splits return the same answer: the value split at $u=\vec e_z$, the three splits by pairs of coefficients, the row split of the matrix model and the column split.

**Where the declared unit does work.** The two-sided form of the same equation, $-(\tilde\nabla^{\natural})_\PhiF-i\bar F\vec e_zk_m=0$, has a mass term that multiplies on the right and conjugates the coefficient. The conjugation reverses the value, because it sends the central $i$ to $-i$ and leaves the units alone, so the two-sided equation can be split by a definite-value pair where the one-sided pair cannot. That is the structural reason the corpus keeps two forms of the equation and does not identify them.

**What this article uses.** The letters $L$ and $R$ below are the pair's components in the sense of §*The Pair's Two Components*. No unit is declared and no value is tested, except where a counterexample is being exhibited.

## Massive Plane Waves: the Field Is Free and the Split Is Fixed

### The Polarization and the Split

For a plane wave $\tilde\Xi_{\mathrm{sp}}=\tilde\Xi_{\mathrm{sp},0}\exp(i\theta)$ with $\theta=\vec k_\Phi\cdot\vec r-k'_tr'_t$ and $\tilde K_{\Phi}=ik'_te_t+\vec k_\Phi$, the gradient acts as left multiplication by $i\tilde K_{\Phi}$ and its conjugate as left multiplication by $i\tilde K_{\Phi}^{\natural}$. The pair becomes

$$
i\tilde K_{\Phi}\tilde\Xi_{\mathrm{sp},0,R}=k_m\tilde\Xi_{\mathrm{sp},0,L},
\qquad
i\tilde K_{\Phi}^{\natural}\tilde\Xi_{\mathrm{sp},0,L}=k_m\tilde\Xi_{\mathrm{sp},0,R}.
$$

Eliminating one component gives $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}\tilde\Xi_{\mathrm{sp},0,R}=-k_m^{2}\tilde\Xi_{\mathrm{sp},0,R}$, so the mass shell is $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_m^{2}$. Write

$$
A=e_t+\frac{i}{k_m}\tilde K_{\Phi},
\qquad\text{so that}\qquad
\tilde\Xi_{\mathrm{sp},0}=A\,\tilde\Xi_{\mathrm{sp},0,R}.
$$

*Proposition.* Let the mass shell hold, $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_m^{2}$, and let $N(A)\neq0$. Then the solutions of the momentum-space system are exactly the pairs

$$
\tilde\Xi_{\mathrm{sp},0,R}=\tilde X,
\qquad
\tilde\Xi_{\mathrm{sp},0,L}=\frac{i}{k_m}\tilde K_{\Phi}\tilde X,
\qquad
\tilde X\in\mathbb{B},
$$

with $\tilde\Xi_{\mathrm{sp},0}=A\tilde X$, and the map $\tilde X\mapsto\tilde\Xi_{\mathrm{sp},0}$ is a bijection.

*Proof.* Since $A-e_t=(i/k_m)\tilde K_{\Phi}$, the first line reads $i\tilde K_{\Phi}\tilde X=k_m(A-e_t)\tilde X=k_m\bigl(\tilde\Xi_{\mathrm{sp},0}-\tilde X\bigr)=k_m\tilde\Xi_{\mathrm{sp},0,L}$. For the second, $\tilde\Xi_{\mathrm{sp},0,L}=(A-e_t)\tilde X=(i/k_m)\tilde K_{\Phi}\tilde X$, so

$$
i\tilde K_{\Phi}^{\natural}\tilde\Xi_{\mathrm{sp},0,L}=i\frac{i}{k_m}\tilde K_{\Phi}^{\natural}\tilde K_{\Phi}\tilde X=-\frac{1}{k_m}\bigl(-k_m^{2}\bigr)\tilde X=k_m\tilde X ,
$$

using the mass shell in the form $\tilde K_{\Phi}^{\natural}\tilde K_{\Phi}=-k_m^{2}$. Conversely the first line gives $\tilde\Xi_{\mathrm{sp},0,L}=(i/k_m)\tilde K_{\Phi}\tilde\Xi_{\mathrm{sp},0,R}$ for every solution, so every solution is of the stated form. The parametrisation is by $\tilde X$ alone, and $\tilde\Xi_{\mathrm{sp},0}=A\tilde X$ is a bijection of $\mathbb{B}$ because $A$ is a unit.

**What the proposition says.** Every element of the algebra is the polarization of exactly one massive plane-wave solution. The pair constrains the split completely and the field not at all. The natural guess is the opposite one, that a degenerate polarization is a special solution, and it is wrong for the massive plane wave: the eight real components of $\tilde\Xi_{\mathrm{sp},0}$ are free, and the equation spends its two lines on the two components instead.

### The Norm of the Factor

The factor $A$ decides how degeneracy is transported from a component to the field.

*Proposition.* With $\gamma=k'_t/k_m$, the norm of the factor is $N(A)=2(1-\gamma)$.

*Proof.* On the mass shell $\lvert\vec k_\Phi\rvert^{2}=k_t^{\prime\,2}-k_m^{2}$. Write $\tilde K_{\Phi}=ik'_te_t+\vec k_\Phi$, so $(i/k_m)\tilde K_{\Phi}=-(k'_t/k_m)e_t+i\vec k_\Phi/k_m$ and $A=(1-\gamma)e_t+i\vec k_\Phi/k_m$. The norm is the sum of the squares of the four complex coefficients, so $N(A)=(1-\gamma)^{2}-\lvert\vec k_\Phi\rvert^{2}/k_m^{2}$, and substituting $\lvert\vec k_\Phi\rvert^{2}=k_m^{2}(\gamma^{2}-1)$ gives $N(A)=1-2\gamma+\gamma^{2}-\gamma^{2}+1=2(1-\gamma)$.

**The corollary.** Multiplicativity gives

$$
N\bigl(\tilde\Xi_{\mathrm{sp},0}\bigr)=2(1-\gamma)\,N\bigl(\tilde\Xi_{\mathrm{sp},0,R}\bigr),
$$

so a massive plane wave is degenerate exactly when its right component is degenerate, and, since $\gamma\neq1$, exactly when its polarization is a zero divisor. The equation does not select the degenerate solutions and does not forbid them; it transports the cone.

**The count.** The polarization is eight real parameters and the cone is six, so the degenerate polarizations are of real codimension two inside the free field. The momentum contributes three parameters on the mass shell, one for $\lvert\vec k_\Phi\rvert$ and two for its direction, so the degenerate massive plane waves form a family of nine real parameters against the eleven of the general plane wave. Degeneracy is not rare and it is not generic; it is the cone, carried along by the momentum.

### The Rest Frame

At $\vec k_\Phi=0$ the two branches of the mass shell are $k'_t=\pm k_m$, and $\gamma=\pm1$. The factor is

$$
A=\bigl(1-\gamma\bigr)e_t=\begin{cases}0, & k'_t=+k_m,\\[2pt] 2e_t, & k'_t=-k_m.\end{cases}
$$

On the branch $k'_t=+k_m$ the factor vanishes, so $\tilde\Xi_{\mathrm{sp},0}=A\tilde\Xi_{\mathrm{sp},0,R}=0$: the single-frequency plane wave has no polarization, although its two components are separately non-zero and opposite, $\tilde\Xi_{\mathrm{sp},0,L}=-\tilde\Xi_{\mathrm{sp},0,R}$. On the other branch the factor is $2e_t$, a unit, and the field survives.

This asymmetry belongs to the sign convention of the pair and not to the physics: the polarization is the sum of the two components, and at $+k_m$ the two components cancel in that sum. The hypothesis $N(A)\neq0$ of the proposition fails exactly here, and the rest frame is the one momentum at which the map $\tilde X\mapsto\tilde\Xi_{\mathrm{sp},0}$ is not a bijection. The consequence is worth stating once, because it is easy to misread a table of rest-frame solutions: a rest-frame field of this corpus is a superposition of the two branches, one of each sign of the frequency, and no single-frequency rest field of the positive branch exists.

## The Sector $\Sigma_{01}$: a Scaled Projection

### The Condition and Its Form

The first sector is $\Sigma_{01}=\{\tilde\Xi^{2}=\lambda\tilde\Xi,\ \lambda\neq0\}$. Its spectrum is $\{\lambda,0\}$, the two eigenvalues are distinct, and the minimal polynomial $X(X-\lambda)$ is squarefree. The element is $\lambda$ times a non-trivial idempotent, and the idempotent is $\tilde\Pi=\tilde\Xi/\lambda$.

**In components.** With $\vec Z=\vec Q/Q_t$ the element is

$$
\tilde\Xi=Q_t\bigl(e_t+\vec Z\bigr)=2Q_t\,\tilde\Pi,
\qquad
\tilde\Pi=\tfrac12\bigl(e_t+\vec Z\bigr),
\qquad
\langle\vec Z\rangle_{\natural}=-1,
$$

where the last condition says that $\vec Z$ is a unit in the $\natural$ norm; in the quaternion square it reads $\vec Z^{2}=e_t$. Written out on the field it is

$$
Q_x^{2}+Q_y^{2}+Q_z^{2}=-Q_t^{2},
\qquad
Q_t\neq0 .
$$

So a member is a scalar part together with a vector part whose Euclidean square is minus the square of the scalar part. The condition is one complex equation in the three complex coefficients of $\vec Z$, which cuts the six real parameters of $\vec Z$ to four and returns the sector's six real parameters once the scalar part is added back.

**In the matrix model.** Under the isomorphism $\mathbb{B}\cong\mathsf M_2(\mathbb{C})$ the norm is the determinant and $2Q_t$ is the trace. The sector is the set of matrices of rank one with non-zero trace: $\det=0$ is the cone, and rank one follows from $\det=0$ and $\tilde\Xi\neq0$. Cayley–Hamilton then reads $M^{2}=(\operatorname{tr}M)M$, which is the sector's identity with $\lambda=\operatorname{tr}M=2Q_t$. A rank-one matrix with a non-zero trace is a projection up to scale: it selects a line, scales it by $\lambda$, and kills a complementary line. The image of left multiplication by $M$ is the set of elements whose columns lie in the image of $M$, the kernel is the set whose columns lie in the kernel of $M$, and the two are complementary here, because $M^{2}=\lambda M$ with $\lambda\neq0$ leaves nothing in both.

### The Split of a Degenerate Field in This Sector

Take the momentum of §*Massive Plane Waves* with $k_m=1$ and $\vec k_\Phi=\sqrt3\,\vec e_z$, so that $k'_t=2$, $\gamma=2$ and $N(A)=-2$. The inverse factor is

$$
A^{-1}=\tfrac12\bigl(e_t+i\sqrt3\,\vec e_z\bigr),
$$

and the polarization $\tilde\Xi_{\mathrm{sp},0}=\tilde\Pi=\tfrac12(e_t+i\vec e_z)$ gives

$$
\tilde\Xi_{\mathrm{sp},0,R}=\frac{1+\sqrt3}{4}\bigl(e_t+i\vec e_z\bigr),
\qquad
\tilde\Xi_{\mathrm{sp},0,L}=\frac{1-\sqrt3}{4}\bigl(e_t+i\vec e_z\bigr).
$$

Both components are real multiples of the same idempotent, both have vanishing norm, and both are in $\Sigma_{01}$ with the weights $\lambda_R=(1+\sqrt3)/2$ and $\lambda_L=(1-\sqrt3)/2$. The two lines of the pair hold: the first gives $i\tilde K_{\Phi}\tilde\Xi_{\mathrm{sp},0,R}-k_m\tilde\Xi_{\mathrm{sp},0,L}=0$ and the second gives $i\tilde K_{\Phi}^{\natural}\tilde\Xi_{\mathrm{sp},0,L}-k_m\tilde\Xi_{\mathrm{sp},0,R}=0$, both to machine precision. The field has $N=0$, $\tilde\Xi^{2}=\tilde\Xi$ and $Q_t=\tfrac12$, so it is in $\Sigma_{01}$ with $\lambda=1=2Q_t$.

**The parts do not leave the ideal.** The factor $A^{-1}$ multiplies on the left, so both components lie in the left ideal $\mathbb{B}\tilde\Xi_{\mathrm{sp},0}$ generated by the field, which for a $\Sigma_{01}$ element is a minimal left ideal of complex dimension two. The split of a degenerate field mixes no directions that the field did not already carry.

### What Survives and What Does Not

**The word fails and the state does not.** The polar word of the field is $\tilde\Xi=r\,e^{i\alpha}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$, and its scale is read from the norm, $N=\rho e^{2i\alpha}$ with $\rho=r^{2}$. On the cone $N=0$, so $r=0$ and the word has no value. What survives is the pair's own data: the idempotent $\tilde\Pi$ and the weight $\lambda$. The idempotent carries a direction and the weight carries a complex number, and neither is read by the word.

**The two numbers are the trace.** The two numbers that the word would have called amplitude and phase are the modulus and the argument of $\lambda$,

$$
\lvert\lambda\rvert=2\lvert Q_t\rvert,
\qquad
\arg\lambda=\arg Q_t .
$$

The polar companion's density is $\rho=r^{2}$, a quadratic object, and its angle is half the argument of the norm. Here the norm is gone and the reading drops to the trace, which is linear. The factor of two that the companion carries in $N=\rho e^{2i\alpha}$ has no counterpart, which is the algebraic reason the polar word does not extend to this sector.

### The Physical Interpretation

A non-trivial idempotent is a ray. The Hermitian members of the sector, $\tilde\Pi(\pm\vec u)=\tfrac12(e_t\pm i\vec u)$ with $\vec u$ a real unit vector, are the members with real $Q_t$ and imaginary $\vec Z$, and the corpus reads them as the pure states of the spin direction $\vec u$. A null momentum is one of them up to a weight: for a real unit vector $\vec n$ and a real $\kappa$,

$$
i\kappa\,e_t+\kappa\,\vec n=2i\kappa\,\tilde\Pi(-\vec n),
$$

so the massless momentum itself sits in this sector, with $\kappa$ its wave number.

The sector keeps a direction and a weight and has no frame. That is what makes it the sector of a ray and not of a transformation: the idempotent says which plane survives and the weight says how much and with what phase, and neither says how the field is moving. A moving field of this sector has its frame in the momentum, and the momentum's frame is the factor $A$ that the proposition of §*The Norm of the Factor* shows to be blind to degeneracy.

## The Sector $\Sigma_{00}$: a Nilpotent

### The Condition and Its Form

The second sector is $\Sigma_{00}=\{\tilde\Xi^{2}=0,\ \tilde\Xi\neq0\}$. Its only eigenvalue is $0$, its minimal polynomial is $X^{2}$ off the apex, and it has no spectral decomposition at all: no non-trivial idempotent commutes with a non-zero nilpotent.

**In components.** The scalar part vanishes, so the condition falls on the vector part alone:

$$
\tilde\Xi=\vec Q,
\qquad
\vec Q^{2}=0
\quad\Longleftrightarrow\quad
Q_t=0,
\quad
Q_x^{2}+Q_y^{2}+Q_z^{2}=0 .
$$

Written in real coordinates $\vec Q=\vec\rho+i\vec\rho'$ the two equations are $\lvert\vec\rho\rvert=\lvert\vec\rho'\rvert$ and $\vec\rho\cdot\vec\rho'=0$: two real three-vectors of equal length at right angles, which in the electromagnetic reading are the electric and magnetic parts of a null bivector. The sector has four real parameters, one common length, one direction for the first vector and one angle for the second, and the apex is its only point that is not a nilpotent.

**In the matrix model.** The sector is the set of rank-one matrices with zero trace, and Cayley–Hamilton reads $M^{2}=0$ directly.

### The Split of a Degenerate Field in This Sector

With the same momentum, the polarization $\tilde\Xi_{\mathrm{sp},0}=\vec e_x+i\vec e_y$ gives

$$
\tilde\Xi_{\mathrm{sp},0,R}=\frac{1+\sqrt3}{2}\bigl(\vec e_x+i\vec e_y\bigr),
\qquad
\tilde\Xi_{\mathrm{sp},0,L}=\frac{1-\sqrt3}{2}\bigl(\vec e_x+i\vec e_y\bigr).
$$

Both components are again real multiples of the field, both are pure, and both square to zero. The field has $Q_t=0$ and $\tilde\Xi^{2}=0$, so it is in $\Sigma_{00}$, and both lines of the pair hold to machine precision.

**A member, checked.** Take $\tilde\Xi=\vec e_x+i\vec e_y$. Then

$$
\tilde\Xi^{2}=-e_t+i\bigl(\vec e_x\vec e_y+\vec e_y\vec e_x\bigr)+i^{2}\vec e_y^{2}=-e_t+0+e_t=0,
$$

the cross terms cancelling because the quaternion units anticommute.

**The image is the kernel.** In the matrix model the image of left multiplication is the set of elements whose columns lie in the image of $\tilde\Xi$, and the kernel is the set whose columns lie in the kernel of $\tilde\Xi$. Both are of complex dimension two, and the image lies inside the kernel because $\tilde\Xi^{2}=0$. The element sends the algebra onto the plane it kills, and a nilpotent of index two is a shift.

### The Physical Interpretation

The element is pure, and a nilpotent is neither Hermitian nor anti-Hermitian, so it lies in neither $\mathbb{B}_\Phi$ nor $\mathbb{B}_\Psi$. A physical four-momentum has a non-zero scalar part, so no momentum is a nilpotent and this sector carries no momentum of its own.

Two physical objects sit here. The first is the null field strength. Write $\tilde F=i\vec V-\vec W$ with $\vec V$ and $\vec W$ the rescaled electric and magnetic vectors, both real and both pure. Then

$$
\tilde F^{2}=\Bigl[\lvert\vec V\rvert^{2}-\lvert\vec W\rvert^{2}+2i\,\vec V\cdot\vec W\Bigr]e_t ,
$$

so the field is a nilpotent exactly when the two real vectors are perpendicular with equal lengths, which is the radiative field with both invariants zero. The second is the lightlike displacement, the algebraic form of a direction that erases itself in one composition.

The sector has a plane and no weight. Its one complex invariant is the direction of the nilpotent, and a direction is what a null line carries. That is the difference in one sentence: $\Sigma_{01}$ keeps a plane and a complex number, and $\Sigma_{00}$ keeps a plane and no number.

## The Massless Case: Degenerate by Construction

### The One-Sided Fields

At $k_m=0$ the pair decouples, and a plane wave reduces each line to a kernel condition,

$$
\tilde K_{\Phi}\tilde\Xi_{\mathrm{sp},0,R}=0,
\qquad
\tilde K_{\Phi}^{\natural}\tilde\Xi_{\mathrm{sp},0,L}=0 .
$$

A non-zero solution requires $\tilde K_{\Phi}$ to be a zero divisor, that is a null element, which is the massless dispersion relation $k_t^{\prime\,2}=\vec k_\Phi^{2}$. When it holds, each kernel is of complex dimension two.

*Proposition.* Every non-zero solution of either one-sided equation is degenerate.

*Proof.* A non-zero element annihilated by a non-zero element is a zero divisor, and the zero divisors are the elements of vanishing norm. The multiplier here is $\tilde K_{\Phi}$ or its conjugate, and it is non-zero by the mass-shell condition $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=0$ combined with $\tilde K_{\Phi}\neq0$.

**This is the sharp difference from the massive case.** For $m\neq0$ a degenerate solution is a codimension-two condition on a free polarization. For $m=0$ a one-sided solution is degenerate identically, at every momentum and at every amplitude, and there is no regular one-sided solution at all.

### The Kernel and Its Two Lines

Take $\tilde K_{\Phi}=ik\,e_t+k\,\vec e_z$, which is null for every $k$. Its left kernel is spanned by

$$
\vec e_t+i\vec e_z\in\Sigma_{01},
\qquad
\vec e_x+i\vec e_y\in\Sigma_{00},
$$

which is one ray of each sector. A general element of the kernel is a combination $a(\vec e_t+i\vec e_z)+b(\vec e_x+i\vec e_y)$, and $Q_t=a$, so the sector is decided by the coefficient of the first line: the kernel is $\Sigma_{01}$ off one complex line and $\Sigma_{00}$ on it. The whole kernel lies on the cone, and the cone's two sectors meet inside it as two of its lines.

The kernel is a right ideal of complex dimension two, since $\tilde K_{\Phi}(\tilde X\tilde A)=(\tilde K_{\Phi}\tilde X)\tilde A$ for every $\tilde A$, and in the matrix model it is a column. A one-sided massless field is therefore a point of a fixed column, and its polarization is a spinor direction and a scale.

### The Two-Sided Massless Field

A massless field of the corpus's pair carries both components, one from each kernel, and the sum is generically a unit. Take the component $\vec e_y-i\vec e_x$ from the kernel of $\tilde K_{\Phi}$ and the component $\vec e_y+i\vec e_x$ from the kernel of $\tilde K_{\Phi}^{\natural}$. Both have vanishing norm, and their sum is $2\vec e_y$, of norm $4$. Written as a sum of cross terms, $\tilde X_L\tilde X_R^{\natural}=2(e_t+i\vec e_z)$ and $\tilde X_R\tilde X_L^{\natural}=2(e_t-i\vec e_z)$, and the two add to $4e_t$: with both parts on the cone, the whole norm of the sum is the interference of the two parts.

So masslessness does not put the field on the cone. The two parts are degenerate and their sum is not, and the quantity that carries the field's norm is the interference of the two. That is the same cross term the polar companion records as the mass of a sum of two rays seen from the side of the domain.

**The lesson.** *Degenerate solution* means two different things in the two regimes. For $m=0$ it is the definition of a one-sided field. For $m\neq0$ it is a condition on the polarization, of real codimension two, which the equation transports but does not impose.

## The Two Sectors Compared

The two sectors differ at every level, and the table is the whole of the difference.

| | $\Sigma_{01}$ | $\Sigma_{00}$ |
| --- | --- | --- |
| algebraic condition | $\tilde\Xi^{2}=\lambda\tilde\Xi$, $\lambda\neq0$ | $\tilde\Xi^{2}=0$, $\tilde\Xi\neq0$ |
| trace, $2Q_t$ | $\lambda\neq0$ | $0$ |
| spectrum | $\{\lambda,0\}$, distinct | $\{0\}$ |
| minimal polynomial | $X(X-\lambda)$, squarefree | $X^{2}$ |
| components | $Q_x^{2}+Q_y^{2}+Q_z^{2}=-Q_t^{2}$, $Q_t\neq0$ | $Q_t=0$, $Q_x^{2}+Q_y^{2}+Q_z^{2}=0$ |
| matrix model | rank one, non-zero trace | rank one, zero trace |
| image against kernel of $L_{\tilde\Xi}$ | complementary | equal |
| what survives | a plane and a weight $\lambda$ | a plane and no weight |
| real parameters | six | four |
| polar word | absent | absent |
| reading | a ray with a direction and a weight | a null direction with neither |

**One line for each.** $\Sigma_{01}$ is a scaled projection: it selects a plane, scales it, and kills a transversal plane. $\Sigma_{00}$ is a shift: it maps the algebra onto the plane it kills and annihilates its own output.

**Why there is no third.** The two sectors are the two ways for a quadratic to degenerate off the apex: two distinct roots with one of them zero, and a double root at zero. The other two patterns of the four belong to $N\neq0$, where the polar word exists, and the companion treats them. On the cone there is no fifth case, and there is no sector in which the field is degenerate and regular at once.

## What Degeneracy Is Not

**It is not a zero field.** $N=0$ says nothing about the size of the field. The corpus carries three norms, and the definite one is $\langle\tilde Q\rangle_{*}=\lvert Q_t\rvert^{2}+\lvert\vec Q\rvert^{2}$. For the nilpotent $\vec e_x+i\vec e_y$ it is $2$ while $\langle\tilde Q\rangle_{\natural}=0$. The definite norm measures the size and the $\natural$ norm decides the cone, so a field of the cone has a size and no $\natural$ norm.

**It is not a failure of the equation.** The pair still holds, the current is still the bilinear of the field, and the spin is still a bilinear, because each is an expression in the element and needs no word. What is lost is the reading of the element in the word's eight named coordinates.

**It is not a condition the mass imposes.** For a massive plane wave the polarization is free and degeneracy is a free choice of that polarization. For a massless one-sided field it is forced. The word *degenerate* names the field's position relative to the cone, and the equation's only role is to transport that position.

**It is not a single condition on the four components.** The norm is one complex equation, so it is two real equations on eight real numbers. A reader who looks for a single component vanishing looks in the wrong place: what vanishes is the determinant, and the determinant is a sum of products.

## Summary

The degenerate solutions of the biquaternionic Dirac equation are the solutions whose field has vanishing quaternionic norm, and they are classified by the cone.

For a massive plane wave the polarization biquaternion is free. Every element of the algebra is the polarization of exactly one solution, the pair fixes only the split into its two components, and the factor $A=e_t+(i/k_m)\tilde K_{\Phi}$ carries the field to its right component with $N(A)=2(1-\gamma)$. The degenerate massive plane waves are therefore exactly the polarizations on the cone, of real codimension two, carried along by a momentum of three parameters.

The cone has two non-zero sectors. $\Sigma_{01}$ is $\tilde\Xi^{2}=\lambda\tilde\Xi$ with $\lambda\neq0$, a rank-one matrix with non-zero trace, in components $Q_x^{2}+Q_y^{2}+Q_z^{2}=-Q_t^{2}$ at $Q_t\neq0$, of six real parameters; its image and kernel under left multiplication are complementary, and it keeps a plane and a weight. $\Sigma_{00}$ is $\tilde\Xi^{2}=0$ with $\tilde\Xi\neq0$, a rank-one matrix with zero trace, in components an isotropic vector part at $Q_t=0$, of four real parameters; its image equals its kernel, and it keeps a plane and no weight.

The polar word fails on both sectors, because its scale is read from the norm and the norm has vanished. What survives is the trace: the amplitude and the phase of a degenerate field are the modulus and the argument of $\lambda=2Q_t$, a linear object where the word's reading was quadratic.

At $k_m=0$ the two lines decouple and every non-zero one-sided solution is degenerate, at every momentum and every amplitude. The kernel of a null left multiplier is a right ideal of complex dimension two, and inside it the two sectors appear as two lines, one of each. The sum of one component from each kernel is generically a unit, so a massless field with both components is generically regular, and the norm of the sum is the interference of the two parts.

The letters $L$ and $R$ are the pair's two components and are fixed by the equation. They are not a definite-value split: a definite-value pair inserted into the chiral pair forces both components to vanish, for any declared traceless unit and either assignment of signs. That incompatibility is why the two-sided form of the equation, whose mass term conjugates and so reverses the value, is the form in which a definite-value split does work.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $\tilde\Xi_{\mathrm{sp}}=\tilde\Xi_{\mathrm{sp},L}+\tilde\Xi_{\mathrm{sp},R}$ | The Dirac field and the pair's two components |
| $\tilde\Xi_{\mathrm{sp},0}$ | The polarization biquaternion of a plane wave |
| $k_m=mc/\hbar$ | Mass wave number; the reciprocal reduced Compton length |
| $\tilde K_{\Phi}=ik'_te_t+\vec k_\Phi$ | Wave biquaternion; $k'_t=\omega/c$ |
| $\gamma=k'_t/k_m$ | Lorentz factor of the plane wave, on shell |
| $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}$ | Quaternionic norm; the determinant of the matrix model; its zero set is the cone |
| $\langle\tilde Q\rangle_{*}=\lvert Q_t\rvert^{2}+\lvert\vec Q\rvert^{2}$ | Definite Hermitian norm; measures the size, never zero off the apex |
| $Q_t$, $\vec Q$ | Scalar part and vector part of an element |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | Square of the vector part; $N=Q_t^{2}+B^{2}$ |
| $\mathcal N=\{N=0\}$ | The cone of zero divisors |
| $\Sigma_{01}$, $\Sigma_{00}$ | The two non-zero sectors of the cone |
| $\lambda=2Q_t$ | The non-zero eigenvalue of a $\Sigma_{01}$ element; the companion's $c$ |
| $\tilde\Pi=\tilde\Xi/\lambda$ | The idempotent of a $\Sigma_{01}$ element |
| $A=e_t+(i/k_m)\tilde K_{\Phi}$ | The momentum factor; $\tilde\Xi_{\mathrm{sp},0}=A\tilde\Xi_{\mathrm{sp},0,R}$ |
| $u$, $R_u$ | A declared traceless unit with $u^{2}=-e_t$, and its right multiplier |

## Further Reading

- *The Dirac Equation in Biquaternionic Form*, for the chiral pair, the one-sided and two-sided forms, and the argument that the pair's letters name two components and not two values. This article takes the equation from there and adds no term to it.
- *The Polar Form of the Dirac Equation in Biquaternionic Form*, for the word whose domain this article leaves, and for the two families of fields on the cone, the parts of definite value and the one-sided plane waves.
- *The Meaning of N Regularity and Degeneracy*, for the cone, its two strata, its two sectors, and the component forms of $\Sigma_{01}$ and $\Sigma_{00}$ that this article restates.
- *Operator Chirality on the Biquaternion Algebra*, for the operator label, for the decomposition by a declared traceless unit, and for the list of objects that are offered as a home for chirality and are not one.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966; second edition Birkhäuser, 2015), for the null fields of the algebra and the reading of a degenerate spinor as a direction without a frame.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, second edition 2001), for the structure of the zero divisors of a Clifford algebra and the rank-one idempotents that this article's two sectors are.
- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the massive and massless plane waves, the mass shell, and the two branches of the frequency.
