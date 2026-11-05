# __The Two-Sided Derivative over the Biquaternion Algebra: Rank-One Gradients, the Complex Eikonal and the Linear Sector__

## Introduction

The corpus differentiates a biquaternion-valued function in one way only. It writes the element-valued operator $\tilde\nabla=\sum_{\mu}e_\mu\,\partial/\partial Q_\mu$, imposes $\tilde\nabla F=0$, and calls the solutions **regular**; the definitions, the integral theory and the Fueter comparison are *Biquaternion Regular Functions*, *Fueter Theory for Biquaternions* and *Biquaternion Analysis*. The convention is not arbitrary, because the obvious alternative does not work: the quotient $\bigl(F(\tilde Z+\tilde H)-F(\tilde Z)\bigr)/\tilde H$ is ambiguous in a noncommutative algebra and undefined at the zero divisors, and the corpus records both failures in §*The Problem of Differentiability* of *Biquaternion Analysis*.

There is a third definition, and it is neither of those two. Instead of dividing by $\tilde H$, it asks the **differential** to factorise, so that the derivative is not a quotient but a pair of multipliers:

$$
dF=L\,dZ\,R .
$$

This is Scheffers' invariant-differential condition with a factor allowed on each side, the **two-sided** or **semi-derivative** form. Over a division algebra it is nearly empty: the admissible maps are the conformal ones, and over $\mathbb{H}$ the condition says only that the map is a composition of translations, dilations, rotations and inversions. That is the programme's own stated reason for the complexification. The conformal group of a Euclidean space of three or more dimensions is finite-dimensional — fifteen parameters in four — so a class of maps that is nothing but the conformal maps is too narrow to carry a field theory. What widens it is complexification, and only because complexification is what supplies the zero divisors: the multipliers may become singular while the product stays finite, the class of admissible maps grows, and the condition it obeys becomes a nonlinear equation rather than a linear one.

This article states the third definition, proves the two propositions and the corollary that make it usable, and fixes its exact relation to the corpus's own operator. The relation is sharper than "a second convention". The two conditions ask for the **same number of equations**, have the **same characteristic cone**, and differ in **degree**: one is linear in the first derivatives of the field, the other is quadratic. They are two representatives of one characteristic class, and neither contains the other. The degree difference is also less absolute than it looks, because the quadratic condition, restricted to the class the programme actually constructs, comes with a linear equation satisfied by the same functions; that is the central finding of the article and it is what makes the word *sector* in the title honest.

The article is mathematics throughout. The reading of the condition as a primary field equation, and the reason its degree matters physically, belong to the companion article *The Differentiable Field: One Primary Equation and the Linear Sector of the Biquaternion Universe*.

## Three Definitions of the Derivative

### The Quotient and Where It Breaks

The naive definition of the derivative at $\tilde Z_0$ is the limit of a quotient,

$$
F'(\tilde Z_0)=\lim_{\tilde H\to0}\frac{F(\tilde Z_0+\tilde H)-F(\tilde Z_0)}{\tilde H},
$$

and it fails for two independent reasons. The first is that the quotient is ambiguous: $\tilde H^{-1}\Delta F$ and $\Delta F\,\tilde H^{-1}$ are different elements, so there are two derivatives and no reason to prefer either. The second is that $\tilde H^{-1}$ need not exist: the zero divisors have vanishing norm $N(\tilde H)=\tilde H\tilde H^{\natural}=0$ with $\tilde H\neq0$, so the limit cannot even be taken along those directions. *Biquaternion Analysis* develops both failures and adopts the operator route in consequence.

A third and subtler failure is worth naming, because it is the one the two-sided form repairs. The quotient presupposes that a derivative is a **single element** and that differentiability is the existence of that element. In a noncommutative algebra the differential is a linear map, and a linear map need not be a multiplication by an element on either side. The two-sided form drops the presupposition and keeps the invariant differential.

### The Operator Form

The corpus's definition is the operator one. For $F$ of class $C^1$ on an open set of a four-dimensional real subspace, the function is **regular** when

$$
\tilde\nabla F=0,\qquad \tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial Q_\mu},
$$

with the quaternion conjugate $\tilde\nabla^{\natural}=\sum_{\mu}\varepsilon_\mu e_\mu\,\partial/\partial Q_\mu$ and $\varepsilon=(1,-1,-1,-1)$. Two properties matter here and both are immediate from the definition.

**It is linear, and linear over the centre.** If $F_1$ and $F_2$ are regular then so is $\alpha F_1+\beta F_2$ for constants $\alpha,\beta\in\mathbb{C}$, and the solution set is a complex vector space.

**It is scale covariant.** If $F$ is regular then $\lambda F$ is regular for every $\lambda\in\mathbb{C}$, with no condition on $\lambda$. The equation cannot distinguish one amplitude from another, since it contains no term that is not proportional to $F$ or to a derivative of $F$.

The second-order operator it defines is scalar, $\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\Box=\sum_\mu\partial^2/\partial Q_\mu^2$, and every regular function is harmonic, $\Box F=0$.

### The Two-Sided Form

**Definition.** Let $\Omega$ be open in $\mathbb{B}$ and let $F:\Omega\to\mathbb{B}$ be of class $C^1$ in the four complex coordinates. The function **admits a two-sided derivative** at $\tilde Z\in\Omega$ when there are elements $L(\tilde Z),R(\tilde Z)\in\mathbb{B}$, neither zero, with

$$
dF=L\,dZ\,R \qquad\text{for every } dZ\in\mathbb{B}.
$$

$L$ and $R$ are the **left and right semi-derivatives**. They are determined by $F$ only up to the equivalence

$$
L\longmapsto L\alpha,\qquad R\longmapsto \alpha^{-1}R,\qquad \alpha\in\mathbb{C}e_t,
$$

the parameter lying in the **centre** and not in the algebra, because only a central element commutes past $dZ$ on both sides. The freedom is therefore one complex parameter, and the pair $(L,R)$ is a projective object.

Two features of the definition are the whole of its interest. **No inverse is taken**: the condition is a statement about products, so a zero divisor causes no difficulty, and the multipliers themselves may be zero divisors. And **the condition is not linear in $F$**: the set of functions admitting a two-sided derivative is not a vector space, and the sum of two such functions need not be one.

### The Three Compared

The table states what each definition demands and what it gives. The third row is the subject of the rest of the article; the first two are the corpus's.

| Definition | Condition | Linear in $F$? | Uses an inverse? | Solutions |
|---|---|---|---|---|
| Quotient | $dF=\Phi\,d\tilde Z$, one-sided | yes | yes, and it must exist | affine maps only |
| Operator | $\tilde\nabla F=0$ | yes | no | a complex vector space, infinite-dimensional |
| Two-sided | $dF=L\,dZ\,R$ | no | no | the eikonal's class, one twistor coordinate, with the four components sharing $L$ and $R$ |

The three are not three conventions for one object. The first is empty beyond the affine maps, and the interesting comparison is between the second and the third.

## The Rank-One Criterion

### The Matrix Form of the Condition

The algebra is $\mathbb{B}\cong M_2(\mathbb{C})$, so the variable and the function are two-by-two matrices of complex functions. Writing the entries of $Z$ as

$$
Z=\begin{pmatrix}\upsilon & w\\ p & v\end{pmatrix},
$$

the four complex coordinates are $\upsilon,v,w,p$ themselves, and $F$ is four functions $F_{CD}$ of those four variables. The differential is the four-by-four array whose entry is the derivative of one component with respect to one coordinate, $\partial F_{CD}/\partial Z_{AB}$, the indices $A,B$ naming the coordinate and $C,D$ the component.

In these indices the two-sided condition reads

$$
\frac{\partial F_{CD}}{\partial Z_{AB}}=L_{CA}R_{BD}.
$$

For a fixed component, that is, for fixed $C$ and $D$, the right-hand side is a product of a column indexed by $A$ and a row indexed by $B$. This is the observation the whole article turns on.

### The Rank-One Criterion

**Proposition 1 (the rank-one criterion).** Let $F$ be $C^1$. If $F$ admits a two-sided derivative with multipliers $L$ and $R$, then for every component $\Sigma=F_{CD}$ the two-by-two matrix

$$
\mathsf D\Sigma:=\begin{pmatrix}\dfrac{\partial\Sigma}{\partial\upsilon} & \dfrac{\partial\Sigma}{\partial w}\\[2pt] \dfrac{\partial\Sigma}{\partial p} & \dfrac{\partial\Sigma}{\partial v}\end{pmatrix}
$$

has rank at most one.

*Proof.* If $dF=L\,dZ\,R$ then, in the indices, $\partial\Sigma/\partial Z_{AB}=L_{CA}R_{BD}$ for the fixed pair $(C,D)$, which is a column times a row and therefore has rank at most one. Conversely, a two-by-two matrix of rank at most one is a column times a row; factorising the matrix of each component gives $\partial\Sigma/\partial Z_{AB}=\varphi_A\psi_B$ for that component, which is the condition with the multipliers depending on the component index. The two factorisations need not agree on a common pair $(L,R)$ across the four components. The criterion is therefore exact for the condition read **component by component**, and it is necessary and not sufficient for the condition with one pair shared by the four components.

For a two-by-two matrix, rank at most one is the vanishing of the determinant, and rank zero is the case of a component whose gradient vanishes. So the criterion is one complex equation per component: **four complex first-order equations** on four unknown functions of four variables.

### The Gradient Is a Zero Divisor

**Proposition 2.** For any $C^1$ function $\Sigma$ of the four coordinates,

$$
\det\mathsf D\Sigma=\tfrac14\,N\bigl(\nabla\Sigma\bigr),
$$

with the norm read in the Cartesian coordinates of complexified Minkowski space,

$$
N\bigl(\nabla\Sigma\bigr)=\left(\frac{\partial\Sigma}{\partial z_0}\right)^2-\left(\frac{\partial\Sigma}{\partial z_1}\right)^2-\left(\frac{\partial\Sigma}{\partial z_2}\right)^2-\left(\frac{\partial\Sigma}{\partial z_3}\right)^2,
$$

and the coordinates given by

$$
z_0=\tfrac12(\upsilon+v),\qquad z_3=\tfrac12(\upsilon-v),\qquad z_1=\tfrac12(w+p),\qquad z_2=\tfrac{i}{2}(w-p).
$$

The first is the scalar coordinate $Q_t$; the other three are $-i$ times the vector coordinates, $z_k=-iQ_k$, which is why the all-plus sum $\sum_\mu(\partial\Sigma/\partial Q_\mu)^2$ and the indefinite sum above are one form written in two frames.

*Proof.* The chain rule gives $\partial/\partial\upsilon=\tfrac12(\partial/\partial z_0+\partial/\partial z_3)$, $\partial/\partial v=\tfrac12(\partial/\partial z_0-\partial/\partial z_3)$, $\partial/\partial w=\tfrac12(\partial/\partial z_1+i\,\partial/\partial z_2)$ and $\partial/\partial p=\tfrac12(\partial/\partial z_1-i\,\partial/\partial z_2)$. Writing $a_\mu:=\partial\Sigma/\partial z_\mu$, the four entries of $\mathsf D\Sigma$ are therefore $\tfrac12(a_0+a_3)$, $\tfrac12(a_0-a_3)$, $\tfrac12(a_1+ia_2)$ and $\tfrac12(a_1-ia_2)$, and the determinant is the difference of two products of sums and differences:

$$
\det\mathsf D\Sigma=\tfrac14(a_0+a_3)(a_0-a_3)-\tfrac14(a_1+ia_2)(a_1-ia_2)=\tfrac14\left(a_0^2-a_3^2-a_1^2-a_2^2\right)=\tfrac14N(\nabla\Sigma),
$$

the sign of the last two terms being the one the factor $i$ supplies.

The identity was verified here on 100 generic complex points, with a largest residual of $1.4\times10^{-14}$ — round-off, since the identity is algebraic once the derivatives are known.

**Corollary.** The two-sided condition on a component is $N(\nabla\Sigma)=0$. The biquaternion gradient of every component is therefore a **zero divisor or zero**, since $N$ is the determinant of the matrix model and the determinant is the biquaternion norm.

### The Four Equivalent Forms

The four forms say one thing. The first is the algebraic one, the second the metric one, the third the one the corpus names, and the fourth the one a differential geometer would write.

| Form | Statement | Where the corpus owns it |
|---|---|---|
| Rank | $\operatorname{rank}\mathsf D\Sigma\le1$ | this article |
| Determinant | $\det\mathsf D\Sigma=0$ | this article |
| Norm | $N(\nabla\Sigma)=0$ | *Norm and Unitary Conventions* |
| Cone | $\nabla\Sigma$ lies on the zero-divisor cone | *Zero Divisors and Units in the Biquaternion Algebra*; *The Topology of the Zero-Divisor Cone* |

The equivalence of the second and third forms is the identity $\det\mathsf M_2(\tilde Q)=N(\tilde Q)$, verified here on 100 random biquaternions with a largest residual of $1.3\times10^{-15}$.

## The Complex Eikonal

### The Coordinate Form

Writing the corollary in the Cartesian coordinates of the proposition gives the equation the condition imposes on each component,

$$
\left(\frac{\partial\Sigma}{\partial z_0}\right)^2-\left(\frac{\partial\Sigma}{\partial z_1}\right)^2-\left(\frac{\partial\Sigma}{\partial z_2}\right)^2-\left(\frac{\partial\Sigma}{\partial z_3}\right)^2=0 .
$$

This is the **complex eikonal** of complexified Minkowski space. It is first order, because it involves the first derivatives only, and quadratic, because it involves their squares. The determinant identity is a chain-rule computation. What the algebra supplies is the arrangement: four coordinates in a two-by-two array, so that the determinant of the first derivatives is a quadratic form in four variables and reads as a metric.

### The Characteristic Reading

The eikonal has a second reading that ties it to the corpus's operator, and the tie is exact.

The principal symbol of $\tilde\nabla$ at a covector $\zeta$ is the matrix $S(\zeta)=\sum_{\mu}\zeta_\mu\mathsf M_2(e_\mu)$. Its determinant is the norm,

$$
\det S(\zeta)=N(\zeta)=\sum_{\mu}\zeta_\mu^2,
$$

because the determinant of the matrix model is the biquaternion norm. The **characteristic set** of $\tilde\nabla$, that is, the set of covectors at which the symbol is singular, is therefore the zero-divisor cone, and the eikonal is the statement that the symbol is singular **at the gradient**:

$$
N(\nabla\Sigma)=0\quad\Longleftrightarrow\quad \det S(\nabla\Sigma)=0 .
$$

So the two-sided condition says that the gradient of every component is a characteristic covector of the corpus's own operator. This is the precise sense in which the two definitions are not rivals: they are built on the same cone.

### What the Eikonal Is Not

Four statements belong here, because each is a natural over-reading.

**It does not imply $\Box\Sigma=0$ — but the programme's own solutions satisfy both.** Both halves of that sentence are needed, and separating them is the sharpest statement in this section.

*The eikonal alone does not make a function harmonic.* The d'Alembertian is built from the same symbol, but a symbol that vanishes at the gradient says nothing about the divergence of the gradient. In the null coordinates $\upsilon,v,w,p$ the two read

$$
\frac{\partial\Sigma}{\partial\upsilon}\frac{\partial\Sigma}{\partial v}=\frac{\partial\Sigma}{\partial w}\frac{\partial\Sigma}{\partial p},
\qquad
\Box\Sigma=4\left(\frac{\partial^2\Sigma}{\partial\upsilon\partial v}-\frac{\partial^2\Sigma}{\partial w\partial p}\right),
$$

so a witness is any function whose four derivatives are non-zero, whose separated products agree and whose d'Alembertian does not vanish:

$$
\Sigma=\sqrt{\upsilon v}+\sqrt{wp},\qquad
\frac{\partial\Sigma}{\partial\upsilon}\frac{\partial\Sigma}{\partial v}=\tfrac14=\frac{\partial\Sigma}{\partial w}\frac{\partial\Sigma}{\partial p},\qquad
\Box\Sigma=(\upsilon v)^{-1/2}-(wp)^{-1/2}\neq0 .
$$

The quantity $\lvert\Box\Sigma\rvert$ vanishes only where $\upsilon v=wp$, a codimension-one locus and not the domain. Checked at 20 random complex points: the eikonal held to $6\times10^{-14}$, the finite-difference floor, and the smallest value of $\lvert\Box\Sigma\rvert$ was $0.64$.

*The class the programme actually uses satisfies both.* The reason is that the rank-one factor is not an arbitrary pair of spinors but the twistor spinor itself. Write $\kappa_0=wG+\upsilon$ and $\kappa_1=vG+p$, let $\Pi_1=\partial\Pi/\partial\kappa_0$ and $\Pi_2=\partial\Pi/\partial\kappa_1$, and differentiate $\Pi(G,\kappa_0,\kappa_1)=0$ in each coordinate, with $\partial\Pi/\partial\upsilon=\Pi_1$, $\partial\Pi/\partial w=G\Pi_1$, $\partial\Pi/\partial p=\Pi_2$ and $\partial\Pi/\partial v=G\Pi_2$. The four derivatives of $G$ come out in closed form, and the ratio within each pair gives the two first-order relations

$$
\frac{\partial G}{\partial w}=G\,\frac{\partial G}{\partial\upsilon},\qquad \frac{\partial G}{\partial v}=G\,\frac{\partial G}{\partial p} ,
$$

identically in $\Pi$; the general solution carries the four relations and the reason no numerical error enters them.

For $\Sigma=G$, these are the rows of the condition $\mathsf D\Sigma=\varphi\psi$ with the right factor the spinor $(1,G)$ and the left factor $\varphi=(\partial G/\partial\upsilon,\partial G/\partial p)$: the right semi-derivative of a twistor-generated solution is the twistor spinor in the gauge $\psi_0=1$. Multiplying the first by $\partial G/\partial p$ and the second by $\partial G/\partial\upsilon$ gives the eikonal; subtracting their cross-derivatives gives

$$
0=\frac{\partial}{\partial w}\left(\frac{\partial G}{\partial v}-G\frac{\partial G}{\partial p}\right)-\frac{\partial}{\partial v}\left(\frac{\partial G}{\partial w}-G\frac{\partial G}{\partial\upsilon}\right)
=\left(\frac{\partial G}{\partial v}\frac{\partial G}{\partial\upsilon}-\frac{\partial G}{\partial w}\frac{\partial G}{\partial p}\right)+G\left(\frac{\partial^2G}{\partial\upsilon\partial v}-\frac{\partial^2G}{\partial w\partial p}\right),
$$

and the bracket is the eikonal, so the second term vanishes: $G\,\Box G=0$. On the quadratic Kerr generating function $\Pi=wG^2+(\upsilon-v+2ia)G-p$ the four derivatives are exact rational functions of the coordinates. Substituting them into $\Box G=4\left(\partial^2G/\partial\upsilon\partial v-\partial^2G/\partial w\partial p\right)$, with the chain rule through the hidden dependence on $G$, and simplifying returns zero identically; the first-order relations and the eikonal likewise close to zero, and hold numerically at 45 working digits to $6\times10^{-32}$ and $2\times10^{-32}$. The second derivative is settled symbolically and not numerically, because a second difference cannot distinguish a vanishing $\Box G$ from one of the order of the step size.

The consequence is worth stating plainly, because it cuts against the obvious reading of a nonlinear equation. **The nonlinearity of the eikonal is inert on the solution class the programme constructs.** The class is generated by an algebraic constraint, the constraint forces the gradient to factorise through the spinor, and the factorisation delivers the eikonal and the wave equation together. What the equation is not, is the source of the linearity: the linear equation is not a short-wavelength limit of the eikonal here, it is a consequence of the algebraic constraint that defines the class. The algebrodynamical article records the same mechanism from the field side, where $\ln G$ is harmonic and its second derivatives are the electromagnetic strengths.

**It is homogeneous of degree two, so it is scale covariant componentwise.** For any function $\Sigma$ and any constant $\lambda$, $N(\nabla(\lambda\Sigma))=\lambda^2N(\nabla\Sigma)$, so a component may be rescaled freely. The condition does not by itself fix an amplitude.

**It is not additive.** For two gradients $g_1,g_2$ with $N(g_1)=N(g_2)=0$, the norm of the sum is the polar form, $N(g_1+g_2)=2\langle g_1,g_2\rangle$, which does not vanish in general. On 100 random pairs of complex null gradients normalised to $\sum_\mu\lvert g_\mu\rvert^2=1$, the smallest value of $\lvert N(g_1+g_2)\rvert$ was $0.063$ against a median of $0.96$, so the failure is neither rare nor small. The solution set of the eikonal is not a vector space, and this is the structural difference from the operator form that no choice of notation can remove.

**It is conformally invariant, and this needs no weight.** The condition is homogeneous of degree two in the gradient, so under a conformal rescaling of the metric $N\mapsto\Omega^{-2}N$ and the zero set is unchanged. The solution set of the eikonal is therefore preserved by the full conformal group of the four-dimensional complex space, not only by the group of complex rotations, and it is preserved without attaching a conformal weight to $\Sigma$; the operator condition is conformally covariant only with a weight on $F$.

## The General Solution

### The Reduction to One Twistor Coordinate

The rank-one criterion can be solved rather than merely imposed, and the solution is algebraic. The construction takes two steps, with two remarks after them.

**Functions of one coordinate.** If $G$ is any function satisfying the eikonal and $f$ is any holomorphic function of one variable, then $\Sigma=f(G)$ satisfies it too, because the chain rule gives $N(\nabla\Sigma)=f'(G)^2N(\nabla G)$ and the square of the derivative multiplies a zero. The class is therefore closed under composition with a holomorphic function.

**The implicit construction.** Let $\Pi(G,\kappa_0,\kappa_1)$ be any holomorphic function of three arguments, and let $G$ be defined implicitly by

$$
\Pi\bigl(G,\;wG+\upsilon,\;vG+p\bigr)=0 .
$$

Then $G$ satisfies the complex eikonal wherever the composite derivative $\Delta$ below is non-zero, and the proof is the implicit function theorem rather than a computation. Write $\Pi_1,\Pi_2$ for the derivatives of $\Pi$ in its second and third arguments and differentiate the defining equation in $\upsilon$:

$$
\Pi_G\,\frac{\partial G}{\partial\upsilon}+\Pi_1\left(w\,\frac{\partial G}{\partial\upsilon}+1\right)+\Pi_2\,v\,\frac{\partial G}{\partial\upsilon}=0 ,
$$

and the same in the other three variables. With $\Delta:=\Pi_G+w\Pi_1+v\Pi_2$, the derivative of the composite $\Pi(G,wG+\upsilon,vG+p)$ with respect to $G$ at fixed coordinates, the four solutions are

$$
\frac{\partial G}{\partial\upsilon}=-\frac{\Pi_1}{\Delta},\qquad \frac{\partial G}{\partial w}=-\frac{G\Pi_1}{\Delta},\qquad \frac{\partial G}{\partial v}=-\frac{G\Pi_2}{\Delta},\qquad \frac{\partial G}{\partial p}=-\frac{\Pi_2}{\Delta} ,
$$

so that $\partial G/\partial w=G\,\partial G/\partial\upsilon$ and $\partial G/\partial v=G\,\partial G/\partial p$ **identically**, for every $\Pi$ and with no numerical error at all. Multiplying the first relation by $\partial G/\partial p$ and the second by $\partial G/\partial\upsilon$ gives $\partial G/\partial\upsilon\,\partial G/\partial v=\partial G/\partial w\,\partial G/\partial p$, the eikonal; cross-differentiating the two gives the wave equation. This is the classical reduction of the eikonal to an arbitrary function of three variables, and the relations were checked against a Newton solve as well: on 37 of 40 random quartics the solve converged and the differentiated $G$ reproduced them to $1.4\times10^{-9}$ relative, the accuracy of the difference.

**The solutions and the branch set.** Resolving $\Pi=0$ for $G$ gives the solution, two-valued for the quadratic $\Pi$ of the Kerr example and multivalued in general. The resolution fails where $\Delta=0$, and that locus is the branch set of $G$: the caustic of the congruence, the locus on which the derivative of the component is infinite, and, in the programme, the locus identified with a particle. Solving $\Pi=0$ together with $\Delta=0$ gives it in closed form. That the construction yields every almost-everywhere analytic solution is the programme's claim, on the authority of its earlier work on the eikonal, and is not established here.

**The count.** The arbitrary datum is the function $\Pi$ of three arguments, and the composed $f$ adds no freedom, since it is one function of one argument. That is the count a single first-order equation in four variables requires, which is the reason the construction is a reduction of the eikonal rather than a family of special solutions inside it.

The three arguments of $\Pi$ are the independent components of a projective twistor in the affine gauge $\psi_0=1$: with $\pi=(1,G)$ the two components $\kappa_0,\kappa_1$ are those of $\omega=Z\pi$, so the pair $(\omega,\pi)$ obeys the Klein–Penrose incidence relation and $\Pi=0$ is an equation on a twistor. *Twistor Theory and Biquaternions* writes the same relation as $\omega=i\,x\pi$, the factor $i$ being the corpus's rescaling of the vector coordinates; the reading of $G$ as a projective spinor ratio is there as well and is not repeated.

### What the Class Contains

The class is large in one direction and narrow in another, and the difference is the practical content of the reduction.

| Function | Two-sided? | Reason |
|---|---|---|
| $Z$ itself | yes | $dF=dZ$, so $L=R=e_t$ |
| $f(G)$ for holomorphic $f$, $G$ resolved from $\Pi$ | yes | chain rule, with $N(\nabla G)=0$ |
| $\upsilon$, $v$, $w$, $p$ | yes | constant gradient of rank one |
| $f(\upsilon,w)$ for any $f$ | yes | the second row vanishes, $\partial/\partial v=\partial/\partial p=0$ |
| $Z_{00}Z_{11}=\upsilon v$ | no | $\det\mathsf D\Sigma=\upsilon v$ |
| a component of $Z^2$, $\upsilon^2+wp$ | no | $\det\mathsf D\Sigma=-wp$ |
| $F=A^2$ with $A=Q_t+\vec e_xQ_x$ | no | the scalar component has $\det\mathsf D\Sigma=z_0^2-z_1^2$ |

Of the three non-examples, one is checked and two are immediate. The component $\upsilon^2+wp$ of $Z^2$ was checked on 100 random points against the closed form $-wp$, with a largest residual of $1.4\times10^{-9}$; the determinant of $\upsilon v$ is $\upsilon v$ by inspection; and the determinant $z_0^2-z_1^2$ of the single-plane witness vanishes exactly on the two planes $z_0=\pm z_1$. The four coordinate entries need no check, their gradients being constant. The class is not closed under multiplication: the product of two functions of $G$ is a function of $G$ and stays in, but the product $\upsilon v$ of two coordinate entries from different rows does not. What the class contains is an arbitrary function of three twistor arguments, carrying a coordinate that solves an algebraic equation — not a ring of functions.

## The Linear Sector

### Three Things Called Linear

The word linear is used of three different objects in this neighbourhood, and they are not the same object. The distinction is the reason the phrase "the linear sector" needs a definition rather than an appeal to intuition.

**Linear multipliers.** If $L$ and $R$ are constrained to be constants, the condition $dF=L\,dZ\,R$ is solved by the affine maps $F=L\,\tilde Z\,R+\tilde C$ and by nothing else, since the differential of any other function depends on $\tilde Z$. The constant-multiplier case is a finite-dimensional family, not a solution space of a differential equation, and it is not the corpus's linear theory.

**A linear equation.** The corpus's condition $\tilde\nabla F=0$ is linear in $F$ with constant coefficients, and its solution space is infinite-dimensional. This is the object the phrase refers to in this article.

**A linearisation.** Linearising the eikonal about one of its solutions gives $2\langle\nabla\Sigma,\nabla\delta\Sigma\rangle=0$, the polar form of the quadratic form taken between the gradient of the solution and the gradient of the perturbation. It is first order with **variable** coefficients, the coefficients being the gradient of the solution, and it is the transport equation along the rays. This is neither of the other two. It has the degree of the corpus's condition and none of its constancy, and it is not the wave equation, which is second order; on the two-sided class the wave equation comes from the twistor constraint rather than from a linearisation, as §*What the Eikonal Is Not* shows.

The three are separated once and for all by that list: constants in the multipliers, constant coefficients in the equation, and constant coefficients nowhere.

### The Same Equations and the Same Cone

Set the two conditions side by side. The comparison is a table of counts, and the counts are what make the relation exact.

| | Operator form | Two-sided form |
|---|---|---|
| Equation | $\tilde\nabla F=0$ | $\det\mathsf D\Sigma=0$ per component |
| Complex equations | four | four |
| Unknowns | four components of four variables | four components of four variables |
| Degree in the first derivatives | one | two |
| Characteristic set | $N(\zeta)=0$ | $N(\nabla\Sigma)=0$ |
| Linear in $F$ | yes | no |
| Solutions obey a linear equation | that equation | yes, $\Box\Sigma=0$ on the twistor class |
| Solution set | a complex vector space | not a vector space |

The rows that agree are the ones that matter, and three of them agree. The count agrees because the operator equation is four complex equations, one per component of the value, and the two-sided condition is four complex equations, one per component as well. The characteristic set agrees because the determinant of the symbol matrix is the norm, which is the same quadratic form the eikonal imposes on the gradient. And the linearity survives in a weaker but real form: the programme's solutions satisfy the wave equation as well as the eikonal, so the two conditions differ in degree rather than in linearity. Two first-order conditions with the same count of equations, the same cone and a common harmonic sector are as close as two different equations of this kind can be.

### Neither Condition Contains the Other

Two witnesses settle the containment question, one for each direction.

**A two-sided function that is not regular.** Take $F=\tilde Z$, the identity. Then $dF=dZ$, so the two-sided condition holds with $L=R=e_t$, and every component has a constant gradient of rank one. But

$$
\tilde\nabla\tilde Z=\sum_{\mu}e_\mu\frac{\partial}{\partial Q_\mu}\sum_{\nu}Q_\nu e_\nu=\sum_{\mu}e_\mu e_\mu=e_t-3e_t=-2e_t\neq0,
$$

so the identity is not regular. The two-sided class is not contained in the regular class.

**A regular function that is not two-sided.** Take the single-plane holomorphic function $F=A^2$ with $A=Q_t+\vec e_xQ_x$, which is regular by the single-plane criterion of *Biquaternion Regular Functions*, its dependence on two of the four variables reducing $\tilde\nabla F=0$ to the Cauchy–Riemann equation in $A$. Its scalar component is $\Sigma=Q_t^2-Q_x^2=z_0^2+z_1^2$, whose array has $\partial\Sigma/\partial\upsilon=\partial\Sigma/\partial v=z_0$ and $\partial\Sigma/\partial w=\partial\Sigma/\partial p=z_1$, so $\det\mathsf D\Sigma=z_0^2-z_1^2$ and the determinant vanishes only on the two planes $z_0=\pm z_1$. The regular class is not contained in the two-sided class.

So the two conditions are genuinely independent. What they share is the cone and the count; what separates them is the degree, and with the degree everything that follows from linearity.

## Summary

The corpus differentiates by an operator, $\tilde\nabla F=0$. The alternative is to require the differential to factorise, $dF=L\,dZ\,R$, and it needs no inverse, so neither noncommutativity nor the zero divisors obstruct it. For each component the condition is that the two-by-two array of its four coordinate derivatives has rank at most one; the determinant of that array is a quarter of the norm of the biquaternion gradient, so the condition is $N(\nabla\Sigma)=0$, the complex eikonal, and it says that the gradient of every component is a zero divisor.

The two conditions have the same number of complex equations, four, and the same characteristic cone, the zero-divisor cone, since the determinant of the symbol matrix of $\tilde\nabla$ is the norm. They differ in degree: one is linear in the first derivatives and one is quadratic. Neither contains the other, and the identity $\tilde Z$ and the single-plane holomorphic function $A^2$ are the two witnesses.

The eikonal is scale covariant componentwise, conformally invariant without a weight, and not additive; its solutions are generated, on the programme's account, by an arbitrary function of three twistor arguments, with the coordinate resolved from an implicit equation and an arbitrary holomorphic function of it composed on the outside; its branch set is the locus $\Delta=0$. The solution class the programme actually constructs satisfies $\Box\Sigma=0$ as well, because the rank-one factor is the twistor spinor and the two first-order relations that the algebraic constraint imposes multiply to the eikonal and cross-differentiate to the wave equation. The failure of additivity is therefore what a quadratic condition costs, and it is the only thing it costs: the linear space survives, and the nonlinearity is inert on the class.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, isomorphic to $M_2(\mathbb{C})$ |
| $\tilde Z$, $Z_{AB}$ | The biquaternion variable and its four complex matrix entries |
| $\upsilon$, $v$, $w$, $p$ | The entries $Z_{00}$, $Z_{11}$, $Z_{01}$, $Z_{10}$ |
| $z_0,z_1,z_2,z_3$ | The Cartesian coordinates of complexified Minkowski space |
| $F$, $F_{CD}$ | The biquaternion-valued function and its four components |
| $\Sigma$ | One component $F_{CD}$, a complex-valued function of the four coordinates |
| $L$, $R$ | The left and right semi-derivatives, defined up to a central rescaling |
| $\mathsf D\Sigma$ | The two-by-two array of the four coordinate derivatives of a component $\Sigma$ |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$ | The biquaternionic gradient and its quaternion conjugate |
| $\Box$ | The d'Alembertian, $\sum_\mu\partial^2/\partial Q_\mu^2$ |
| $N(\tilde Q)$ | The biquaternion norm $\sum_\mu Q_\mu^2$, the determinant of $\mathsf M_2(\tilde Q)$ |
| $\langle g_1,g_2\rangle$ | The polar form $\sum_\mu g_{1\mu}g_{2\mu}$ of the norm |
| $\Pi$, $G$, $\kappa_0$, $\kappa_1$ | The generating function, the projective coordinate and the two twistor components |
| $\Delta$ | The derivative $\Pi_G+w\Pi_1+v\Pi_2$ of the composite $\Pi(G,wG+\upsilon,vG+p)$ |
| $A$ | The single-plane variable $Q_t+\vec e_xQ_x$ |

## Further Reading

- [Biquaternion Analysis](biquaternion-analysis.html), for the metric structure, the two obstructions to the quotient derivative and the adoption of the operator route.
- [Biquaternion Regular Functions](biquaternion-regular-functions.html), for the definition of regularity, single-plane holomorphy and the shifted operator.
- [Fueter Theory for Biquaternions](fueter-theory-for-biquaternions.html), for the Fueter construction, the axial extension and the slice approach.
- [The First-Order Root of the Biquaternion D'Alembertian](the-first-order-root-of-the-biquaternion-d-alembertian.html), for the symbol of $\tilde\nabla$, the Clifford relation and the enveloping operator algebra.
- [Zero Divisors and Units in the Biquaternion Algebra](zero-divisors-and-units.html), for the criterion $N=0$ and the two families of the cone.
- [The Topology of the Zero-Divisor Cone](the-topology-of-the-zero-divisor-cone.html), for the cone as a topological object and its Lorentzian slices.
- [Remarkable Subspaces and the Analysis](remarkable-subspaces-and-the-analysis.html), for the restriction of the operator to each real form and the elliptic and hyperbolic cases.
- [The Differentiable Field: One Primary Equation and the Linear Sector of the Biquaternion Universe](../articles_physics/the-differentiable-field-one-primary-equation-and-the-linear-sector.html), the companion article, for the reading of the two-sided condition as a field equation.
- [Twistor Theory and Biquaternions](../articles_physics/twistor-theory-and-biquaternions.html), for the incidence relation $\omega=i\,x\pi$ and the reading of $G$ as a projective spinor ratio.
- [The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry](../articles_physics/the-algebrodynamical-programme-nonlinear-cauchy-riemann-conditions-self-quantized-charge-and-induced-causal-geometry.html), for the source in which the two-sided condition is developed as a physical programme.
- G. Scheffers, "Verallgemeinerung der Grundlagen der gewöhnlichen komplexen Funktionen", *Berichte der Sächsischen Akademie der Wissenschaften* **45** (1893), for the invariant-differential definition of differentiability over an algebra and its one-sided form.
