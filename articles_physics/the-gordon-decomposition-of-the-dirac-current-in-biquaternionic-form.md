# __The Gordon Decomposition of the Dirac Current in Biquaternionic Form__

## Introduction

The **Gordon decomposition** is an identity for the conserved current of a solution of the Dirac equation. It splits the current into two pieces of different physical character: a **convection** part, which is the orbital current carried by the momentum, and a **spin** part, which is the divergence of a spin density and is the source of the magnetisation. The identity is due to Walter Gordon (1926). The spin part is the term whose coefficient fixes the tree-level gyromagnetic factor at $g=2$, and whose radiative correction is the anomalous magnetic moment.

The decomposition is **on shell**. It uses the Dirac equation for the field and for its adjoint, so it holds for solutions and not for arbitrary fields. It also needs a nonzero mass in its covariant form, because the mass divides both terms. The massless case has a separate reading, in which the spin term survives as the curl of the spin density and only the scale changes, from $m$ to $E$.

The field of this article is an element of $\mathbb{B}$ at each point, and its four coefficients are its four components. The current is the **pairing** of the field with the element the generator carries into it, $j_{\imath}=\bar{\tilde{Ξ}}\,i\,e_{\imath}\,\tilde{Ξ}\,\vec e_{\mathrm{spt}(\imath)}$, where the pairing $\bar{\tilde{Ξ}}X=\operatorname{Sc}(\tilde{Ξ}^*iX\vec e_x)$ is a scalar part of a product of elements. No carrier is added to the algebra and no list of components is used: an element, a product and its scalar part.

This article states the identity, proves it, gives its momentum-space form and its massless limit, and reports the two companion objects — the angular-momentum (Belinfante–Rosenfeld) split and the stress tensor. It then gives the biquaternion reading. The contribution here is a matter of **naming the two structures**: the split of a product of two generators into its symmetric part, which is the central direction of the algebra, and its antisymmetric part, which is a bivector and lies in the algebra's six directions $\vec e_\eta$ and $i\vec e_\eta$. The convection current is the central direction; the spin current is the bivector. What the framework does **not** supply is a bilinear in the field and its conjugate alone: the current is a scalar part of three factors, and the third, the frame's unit $\vec e_{\mathrm{spt}(\imath)}$, is not carried by the field. The older spelling hides that datum in the adjoint; written as a pairing it is visible as the last factor.

The article is organised as follows. The next section fixes the conventions: the field and its value, the frame, the pairing, the two Dirac equations and the current. The section after it states the identity and proves it. A section gives the momentum-space form used in scattering. A section reads the two terms physically. A section gives the massless limit and says what survives it. A section records the angular-momentum and stress-tensor relatives and the electromagnetic consequence. A section gives the biquaternion reading. The closing sections are the open questions, the standard Greek names of the same objects, the summary, the notation table and the literature.

## Conventions

### The Field and Its Value

The conventions are those of the companion articles, and none is restated here: the algebra, its basis, its element glyphs and its three conjugations are *Algebra and Element Conventions*; the twelve products and the four forms are *Product and Form Conventions*; the metric and the invertibles are *Frame and Metric Conventions*; the chirality value is *Matrix Representations Conventions*, §*The Subscript on an Element*; the gradient and its four products are *Operator and Calculus Conventions*.

The field is an element of $\mathbb{B}$. At each point $\tilde Q$ it takes a value $\tilde{Ξ}(\tilde Q)$, with the four coefficients $\tilde{Ξ}_{t}$, $\tilde{Ξ}_{x}$, $\tilde{Ξ}_{y}$, $\tilde{Ξ}_{z}$. Those four coefficients are the four components of the field. A state is an element; there is no second carrier behind it, and the four coefficients are read off the one element.

The **value** of an element is a letter with two possibilities, and it is the subscript. The value $L$ is the minus one and the value $R$ the plus one; an element is written $\tilde{Ξ}_{L}$ or $\tilde{Ξ}_{R}$. That is the whole definition, and this article computes nothing from it. Two facts about the value are used, and both are read from the conventions: a product takes the letter of its right factor, and a left multiplication keeps the letter. One consequence is used once, when the massless case is read: right multiplication by $e_t$ or by $\vec e_z$ keeps the value, and right multiplication by $\vec e_x$ or by $\vec e_y$ exchanges the two.

### The Frame

The four **generators** are the actions

$$
\tilde Q\longmapsto i\,e_{\imath}\,\tilde Q\,\vec e_{\mathrm{spt}(\imath)},
\qquad
\mathrm{spt}(t)=x,\quad\mathrm{spt}(\eta)=y .
$$

They are a frame, not the algebra. They are a choice of four actions, made once here and used throughout, and the choice is not a default of the notation. The three spatial units have three different jobs: $\vec e_x$ is the right multiplier of the temporal generator, $\vec e_y$ the common right multiplier of the three spatial ones, and $\vec e_z$ appears in the chirality basis operator and in the current's last factor, and nowhere else in the frame. Each generator carries a spatial unit on the right, so each of the four exchanges the value of an element.

**The axis is a property of the basis, and it is stated once.** An action is diagonal in a basis when it carries each basis element into a multiple of itself. In the coefficient basis the diagonal actions of the sixteen basis operators are exactly four, and they are the four squares, with the eigenvalues

| action | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_te_t$ | $1$ | $1$ | $1$ | $1$ |
| $\vec e_x\vec e_x$ | $-1$ | $-1$ | $1$ | $1$ |
| $\vec e_y\vec e_y$ | $-1$ | $1$ | $-1$ | $1$ |
| $\vec e_z\vec e_z$ | $-1$ | $1$ | $1$ | $-1$ |

The four are unchanged as a set by a permutation of the three units, so the coefficient basis says nothing about any spatial direction: one row carries four pluses and each of the other three carries two minuses, and no row is singled out. The frame above does name three directions in three jobs, and that is the price of using it; it is paid openly, and no sentence of this article lets one of the three pass as though the algebra preferred it.

**The chirality basis operator.** The basis operator that reads the value is the right multiplication by $-i\vec e_z$. It is named here because the two values are the subject of the axial vertex below, and it is used nowhere else.

### The Pairing

The adjoint is not an action on the field: it is a **pairing**, a rule that takes two elements to one number. Derive it once, here. For elements $\tilde{Ξ}$ and $X$, write

$$
\bar{\tilde{Ξ}}\,X:=\operatorname{Sc}\big(\tilde{Ξ}^*\,i\,X\,\vec e_x\big),
$$

with ${}^{*}$ the Hermitian conjugation of *Algebra and Element Conventions* and $\operatorname{Sc}$ the scalar part. The right side is a scalar part of a product of elements, so the pairing is a **derived form** of this article and not a new convention. It is linear in $X$ and conjugate-linear in its first slot. The one datum of the frame it carries is the right multiplier $\vec e_x$, the adjoint's unit; the conjugation alone would need no frame.

The pairing is written on the right of the bar, and it takes the whole product that follows. When the product is a single element the bar reads as an ordinary bilinear; when it is three factors the bar reads the scalar part of the triple product.

### The Two Dirac Equations

The **field equation** is

$$
\sum_{\imath}\varepsilon_{\imath}\,e_{\imath}\,\partial_{\imath}\tilde{Ξ}\,\vec e_{\mathrm{spt}(\imath)}=-2\pi\nu_m\,\tilde{Ξ} .
$$

Every factor is written out: the derivative acts on the field, the unit $e_{\imath}$ multiplies from the left, the frame's unit $\vec e_{\mathrm{spt}(\imath)}$ from the right, and the plain weight $\varepsilon_{\imath}$ of *Frame and Metric Conventions* raises the index of the generator. The weight is not a second metric factor; it is the sign that makes the four generators obey one anticommutation rule.

The component form displays the two families at once, because the temporal generator is a single right multiplication and the three spatial generators share their right multiplier:

$$
\sum_\eta\vec e_\eta\,\partial_k\tilde{Ξ}\,\vec e_y-\partial_t\tilde{Ξ}\,\vec e_x=2\pi\nu_m\,\tilde{Ξ} .
$$

Each of the four terms exchanges the value, while the mass term keeps it: the equation pairs the two halves of the field, and the mass is what pairs them.

The same operator content is written by the series as the chiral pair

$$
\tilde\nabla_\Phi\tilde{Ξ}_{R}=2\pi\nu_m\tilde{Ξ}_{L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=2\pi\nu_m\tilde{Ξ}_{R},
$$

which acts by left multiplication on the algebra (*Algebra and Element Conventions*). The pair and the two-sided equation above carry the same operator content and are not the same statement; the passage from one to the other is a change of representation, and *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* separates the two forms. This article uses the two-sided equation, because the current below is defined against the frame's units. Here $\nu_m=\frac{mc}{h}$ is the mass wave number, the inverse of the mass length.

The second equation is the **adjoint**. Conjugating the field equation and pairing both sides with an arbitrary element $X$ gives

$$
\sum_{\imath}\varepsilon_{\imath}\,\overline{\partial_{\imath}\tilde{Ξ}}\,e_{\imath} X\vec e_{\mathrm{spt}(\imath)}=m\,\bar{\tilde{Ξ}}\,X
\qquad\text{for every }X .
$$

The mass carries the other sign than in the field equation, because the conjugation reverses the sign of the real action while leaving the generator's imaginary unit alone. The two equations are displayed separately because the proof below puts one of them on each side of the current.

### The Current

The **number current** of a solution is

$$
j_{\imath}=\bar{\tilde{Ξ}}\,i\,e_{\imath}\,\tilde{Ξ}\,\vec e_{\mathrm{spt}(\imath)}
=\operatorname{Sc}\big(\tilde{Ξ}^*\,e_{\imath}\,\tilde{Ξ}\,c_{\imath}\big),
\qquad
c_t=e_t,\quad c_k=\vec e_z .
$$

The second form is derived from the first at the place of use. The two imaginary units multiply to $-1$, so $j_{\imath}=-\operatorname{Sc}(\tilde{Ξ}^*e_{\imath}\tilde{Ξ}\vec e_{\mathrm{spt}(\imath)}\vec e_x)$, and the frame's unit is $c_{\imath}:=-\vec e_{\mathrm{spt}(\imath)}\vec e_x$, with $-\vec e_x\vec e_x=e_t$ in the temporal family and $-\vec e_y\vec e_x=\vec e_z$ in the spatial one.

The temporal component is the density, and it needs no frame unit at all:

$$
j_0=\operatorname{Sc}\big(\tilde{Ξ}^*\tilde{Ξ}\big)=\lvert\tilde{Ξ}_{t}\rvert^2+\lvert\tilde{Ξ}_{x}\rvert^2+\lvert\tilde{Ξ}_{y}\rvert^2+\lvert\tilde{Ξ}_{z}\rvert^2 .
$$

That is why the density is positive rather than a sign of the frame. The three spatial components are $j_\eta=\operatorname{Sc}(\tilde{Ξ}^*\vec e_\eta\tilde{Ξ}\vec e_z)$. The index $\mu$ labels the four generators; it is not the index of one object inside the algebra, and the four components are four pairings rather than four slots of a single element. For a solution the four are real, and $j_0$ is positive.

## The Identity

### Statement

Let $\tilde{Ξ}$ be a solution of the field equation of §*The Two Dirac Equations*. The Gordon decomposition splits the current into two terms of different character: a **convection** part, which carries the first derivative of the field itself, and a **spin** part, which is the divergence of the antisymmetric density $\bar{\tilde{Ξ}}\,\Sigma_{\imath\jmath}\tilde{Ξ}$ built from the spin generator defined below.

$$
\boxed{\;
\bar{\tilde{Ξ}}\,i\,e_{\imath}\,\tilde{Ξ}\,\vec e_{\mathrm{spt}(\imath)}
=\frac{i}{4\pi\nu_m}\Big(\bar{\tilde{Ξ}}\,\partial_{\imath}\tilde{Ξ}-\overline{\partial_{\imath}\tilde{Ξ}}\,\tilde{Ξ}\Big)
+\frac{1}{2\pi\nu_m}\sum_{\jmath}\varepsilon_{\jmath}\,\partial_{\jmath}\Big(\bar{\tilde{Ξ}}\,\Sigma_{\imath\jmath}\tilde{Ξ}\Big)\;}
$$

The spin generator $\Sigma_{\imath\jmath}$ is $\frac{i}{4}$ times the commutator of the $\mu$-th and ${\jmath}$-th generators, antisymmetric in its two indices; its action on an element is written $\Sigma_{\imath\jmath}\tilde{Ξ}$. The $i$ is the one the generator already carries. It is $i$ times the Lorentz generator of *Matrix Representations Conventions*, which is half the bivector of the pair; written out, $\Sigma_{23}$ is the left multiplication by $\frac{i}{2}\vec e_x$, and $\Sigma_{01}$ multiplies by $\frac{i}{2}\vec e_x$ on the left and by $\vec e_z$ on the right. The spin term is a total divergence, and the antisymmetry of $\Sigma_{\imath\jmath}$ is what makes it one.

### Proof

The proof uses the two equations, one factor on each side of the current. Pair the field equation from the left with the generator, that is, act on it with $\tilde Q\mapsto ie_{\imath}\tilde Q\vec e_{\mathrm{spt}(\imath)}$ and then pair with $\tilde{Ξ}$:

$$
-m\,j_{\imath}=\sum_{\jmath}\varepsilon_{\jmath}\,\bar{\tilde{Ξ}}\,\big(ie_{\imath}\big(e_{\jmath}\,\partial_{\jmath}\tilde{Ξ}\,\vec e_{\mathrm{spt}(\jmath)}\big)\vec e_{\mathrm{spt}(\imath)}\big).
$$

The product of the two left multipliers is $e_{\imath} e_{\jmath}$ and the product of the two right multipliers is $\vec e_{\mathrm{spt}(\jmath)}\vec e_{\mathrm{spt}(\imath)}$; by the split of a product of two actions in the conventions, the result is $-i$ times the plain weight, less twice the spin generator. Pairing gives

$$
-m\,j_{\imath}=\sum_{\jmath}\varepsilon_{\jmath}\Big(-i\,\varepsilon_{\imath}\delta_{\imath\jmath}\,\bar{\tilde{Ξ}}\,\partial_{\jmath}\tilde{Ξ}-2\,\bar{\tilde{Ξ}}\,\Sigma_{\imath\jmath}\partial_{\jmath}\tilde{Ξ}\Big),
$$

with $\varepsilon_{\imath}\delta_{\imath\jmath}$ the plain weight of *Frame and Metric Conventions*, that is, the scalar part of $e_{\imath} e_{\jmath}$, which is $1$ at ${\jmath}=\mu$ and $0$ otherwise. Put $X=ie_{\imath}\tilde{Ξ}\vec e_{\mathrm{spt}(\imath)}$ in the adjoint equation, so that the generator acts on the field and not on the conjugated factor:

$$
m\,j_{\imath}=\sum_{\jmath}\varepsilon_{\jmath}\Big(-i\,\varepsilon_{\imath}\delta_{\imath\jmath}\,\overline{\partial_{\jmath}\tilde{Ξ}}\,\tilde{Ξ}+2\,\overline{\partial_{\jmath}\tilde{Ξ}}\,\Sigma_{\imath\jmath}\tilde{Ξ}\Big).
$$

Subtracting the second from the first, the mass terms cancel and the two bivector pieces combine into one derivative:

$$
-2m\,j_{\imath}=\sum_{\jmath}\varepsilon_{\jmath}\Big[-i\,\varepsilon_{\imath}\delta_{\imath\jmath}\Big(\bar{\tilde{Ξ}}\,\partial_{\jmath}\tilde{Ξ}-\overline{\partial_{\jmath}\tilde{Ξ}}\,\tilde{Ξ}\Big)
-2\,\partial_{\jmath}\Big(\bar{\tilde{Ξ}}\,\Sigma_{\imath\jmath}\tilde{Ξ}\Big)\Big].
$$

The weight collapses the sum, because $\varepsilon_{\jmath}\varepsilon_{\imath}\delta_{\imath\jmath}$ is $\varepsilon_{\imath}^2=1$ at ${\jmath}=\mu$ and $0$ otherwise, so only the term ${\jmath}=\mu$ survives and the coefficient of the convection bracket is the same $-i$ for all four components. The bivector part is a total derivative because $\Sigma_{\imath\jmath}$ is a constant action and is antisymmetric in its two indices: the derivative of the bilinear is the sum of the two bivector pieces, one with the derivative on each factor. Dividing by $2m$,

$$
j_{\imath}=\frac{i}{4\pi\nu_m}\Big(\bar{\tilde{Ξ}}\,\partial_{\imath}\tilde{Ξ}-\overline{\partial_{\imath}\tilde{Ξ}}\,\tilde{Ξ}\Big)
+\frac{1}{2\pi\nu_m}\sum_{\jmath}\varepsilon_{\jmath}\,\partial_{\jmath}\Big(\bar{\tilde{Ξ}}\,\Sigma_{\imath\jmath}\tilde{Ξ}\Big),
$$

which is the identity as stated. The spin term is the divergence of a bilinear and not the bilinear times a divergence, and that is the content of the last step: the two bivector contributions add into one derivative.

The algebra was checked numerically, on at most a hundred elements. The sixteen basis operators of the coefficient basis are signed permutations of the four coefficients, each of determinant $1$, of Euclidean norm two and mutually orthogonal, exactly; the four diagonal actions are the four squares, with the eigenvalues tabled above, exactly; the product of two generators and the two mixed products of the proof hold with residual zero. The field equation holds to $10^{-16}$ and the adjoint to $5\times10^{-16}$, on a three-mode superposition of on-shell plane waves. The derived form of the current is exact; the position-space identity holds to $7\times10^{-17}$ in all four components; the momentum-space form to $8\times10^{-16}$ over twenty-five random on-shell pairs, its parent identity to $2\times10^{-15}$ and its axial companion to $7\times10^{-16}$. The four components of the current are real on every solution, and the temporal one is positive.

### A note on the total divergence

The spin term is a total divergence, and its own divergence vanishes identically: $\partial_{\imath}\partial_{\jmath}$ is symmetric in the two indices while $\Sigma_{\imath\jmath}$ is antisymmetric, so the spin current is conserved without the field equation being used. It is a **bound** current rather than a transport current. It can be removed from the current at the price of a surface term, it contributes nothing to the total charge, and it cannot be removed from the magnetic moment, which is the integral of the spin density. The convection term is separately conserved on shell, by the two Dirac equations. What the decomposition separates is therefore not a conserved piece and a non-conserved piece, but a transport current and a magnetisation current.

## The Momentum-Space Form

For plane-wave solutions the position-space identity becomes the form used in scattering amplitudes. Write the field of momentum $p$ as

$$
\tilde{Ξ}=\tilde w(p)\,\exp\Big(-i\theta_{\mathrm{pwp}}),
$$

so that $\partial_{\imath}\tilde{Ξ}=-ip_{\imath}\tilde{Ξ}$, and the field equation becomes the on-shell condition

$$
\sum_{\imath}\varepsilon_{\imath}\,p_{\imath}\,i\,e_{\imath}\,\tilde w(p)\,\vec e_{\mathrm{spt}(\imath)}=m\,\tilde w(p).

$$

The angle is $\theta_{\mathrm{pwp}}=\frac{p\cdot x}{h}=\omega r'_t-2\pi\vec\nu_\Phi\cdot\vec r$: a real four-momentum paired with a real position over $\frac{h}{2\pi}$, so the angle is real.

The exponent carries no weight $\varepsilon_{\imath}$. The weight belongs to the contraction of the generator with the momentum, where it raises the generator's index, and the derivative returns $p_{\imath}$ with the same sign for all four components. A weight in the exponent would flip the sign of the three spatial derivatives and would make the position-space and the momentum-space identities disagree on the sign of the spatial convection current.

Write $\bar w_2$ for the pairing of *The Pairing* read at the on-shell momentum $p_2$. It obeys the same condition on the other side,

$$
\sum_{\imath}\varepsilon_{\imath}\,p_{2,\imath}\,\overline{\tilde w(p_2)}\,i\,e_{\imath}\,X\,\vec e_{\mathrm{spt}(\imath)}=m\,\bar w_2\,X
\qquad\text{for every }X .
$$

Between such solutions the Gordon decomposition reads

$$
\boxed{\;
\bar w_2\,i\,e_{\imath}\,w\,\vec e_{\mathrm{spt}(\imath)}
= \frac{(p+p_2)_{\imath}}{2\,m\,c}\,\bar w_2w
+ \frac{i}{m\,c}\sum_{\jmath}\varepsilon_{\jmath}\,(p_2-p)_{\jmath}\,\bar w_2\,\Sigma_{\imath\jmath}w\;}
$$

Equivalently, with the momentum transfer $2\pi\nu_{\jmath}=(p_2-p)_{\jmath}$ and the average momentum $P_{\imath}=\tfrac12(p+p_2)_{\imath}$,

$$
\bar w_2\,i\,e_{\imath}\,w\,\vec e_{\mathrm{spt}(\imath)}
=\frac{1}{m\,c}\Big(P_{\imath}\,\bar w_2w
+ i\sum_{\jmath}\varepsilon_{\jmath}\,2\pi\nu_{\jmath}\,\bar w_2\Sigma_{\imath\jmath}w\Big).
$$

The first term is proportional to the scalar bilinear $\bar w_2w$, the second to the tensor bilinear $\bar w_2\Sigma_{\imath\jmath}w$, and the two coefficients are fixed: $P_{\imath}/m$ and $ik_{\jmath}/m$. This is the form in which the vertex decomposition of the companion article on the anomalous magnetic moment is stated.

### The parent identity

Both momentum-space statements are consequences of the simpler **parent identity**. The two on-shell conditions replace the field on either side of a bilinear by the generator applied to it, so for any two products of invertibles $a$ and $b$

$$
2m\,\bar w_2\,a\,w\,b
= \bar w_2\Big(\sum_{\imath}\varepsilon_{\imath}\,p_{2,\imath}\,i\,e_{\imath}\,a\,w\,b\,\vec e_{\mathrm{spt}(\imath)}\Big)
+ \bar w_2\Big(a\sum_{\imath}\varepsilon_{\imath}\,p_{\imath}\,i\,e_{\imath}\,w\,\vec e_{\mathrm{spt}(\imath)}\,b\Big),
$$

with $a=e_{\imath}$ and $b=\vec e_{\mathrm{spt}(\imath)}$ it gives the Gordon form above. Each parenthesis is a product of elements, and the whole statement is a scalar part of products: it carries no operator symbol.

The two products of the parent identity are read off from the split of a product of two actions, with the momentum contracted into the actions and the imaginary units multiplied out:

$$
\Big(\sum_\rho\varepsilon_\rho\,p_{2,\rho}\,i\,e_\rho\,\cdot\,\vec e_{\mathrm{spt}(\rho)}\Big)\,\big(ie_{\imath}\,\cdot\,\vec e_{\mathrm{spt}(\imath)}\big)
=p_{2,\imath}+2i\sum_{\jmath}\varepsilon_{\jmath}\,\Sigma_{\imath\jmath}\,p_{2,\jmath},
\qquad
\big(ie_{\imath}\,\cdot\,\vec e_{\mathrm{spt}(\imath)}\big)\,\Big(\sum_\rho\varepsilon_\rho\,p_\rho\,i\,e_\rho\,\cdot\,\vec e_{\mathrm{spt}(\rho)}\Big)
=p_{\imath}-2i\sum_{\jmath}\varepsilon_{\jmath}\,\Sigma_{\imath\jmath}\,p_{\jmath}.
$$

Each product is a scalar plus a bivector, and the scalar part is the momentum component of the action that was not contracted. The sum of the two is $(p+p_2)_{\imath}+2i\sum_{\jmath}\varepsilon_{\jmath}\Sigma_{\imath\jmath}(p_2-p)_{\jmath}$, which is $2m$ times the bracket of the momentum-space identity, because the on-shell conditions replace the contracted momenta by $m$.

### The axial companion

The **axial companion** takes the product of a generator with the chirality basis operator: the action $\tilde Q\mapsto ie_{\imath}\tilde Q\vec e_{\mathrm{spt}(\imath)}$ followed by $\tilde Q\mapsto-i\tilde Q\vec e_z$. Two features are worth stating before the algebra. First, it is a **real action**: the two imaginary units multiply to $+1$, so

$$
\big(ie_{\imath}\,\cdot\,\vec e_{\mathrm{spt}(\imath)}\big)\big(-i\,\cdot\,\vec e_z\big)
=e_{\imath}\,\cdot\,\vec e_z\vec e_{\mathrm{spt}(\imath)},
$$

and the axial vertex carries no imaginary unit at all. Second, each generator exchanges the value while a product of two generators keeps it, because the two units $\vec e_x$ and $\vec e_y$ exchange the value and their products are $\pm e_t$ and $\pm\vec e_z$, which keep it. So the chirality basis operator reverses the sign of the weight part of a product and leaves the bivector part alone. That reversal is what exchanges the two slots.

With both products expanded as above and the chirality basis operator moved to the front of each, the sum divided by $2m$ gives

$$
\bar w_2\,e_{\imath}\,w\,\vec e_z\vec e_{\mathrm{spt}(\imath)}
= \frac{(p_2-p)_{\imath}}{2\,m\,c}\,\bar w_2\big(-i\,w\,\vec e_z\big)
+ \frac{i}{m\,c}\sum_{\jmath}\varepsilon_{\jmath}\,(p_2+p)_{\jmath}\,\bar w_2\big(-i\,\Sigma_{\imath\jmath}w\,\vec e_z\big).
$$

The vector identity has the average momentum in the convection slot and the transfer in the spin slot; the axial identity has the transfer in the convection slot and the average momentum in the spin slot. The exchange is not an extra fact about the algebra: it is the minus sign that the exchange of the value puts on the weight term and withholds from the bivector term.

## The Physical Reading

### Convection and spin

The two terms of the momentum-space identity have a direct interpretation, and that is why the decomposition is useful.

The **convection term** is $\frac{(p+p_2)_{\imath}}{2\,m\,c}\bar w_2w$. It is the current of a charged scalar of mass $m$ and momentum $\tfrac12(p+p_2)$: the orbital part. It depends on the average four-momentum, it reduces to $\bar w_2w\,v_{\imath}$ in the non-relativistic limit, and it is the piece protected by gauge invariance.

The **spin term** is $\frac{i}{m\,c}\sum_{\jmath}\varepsilon_{\jmath}(p_2-p)_{\jmath}\bar w_2\Sigma_{\imath\jmath}w$. It depends on the momentum **transfer** and on the tensor bilinear, and it is the piece that carries the magnetic moment: a spin density produces a current only where its density varies, and the variation is what the transfer measures.

The identification of the second term with the spin density is not a metaphor. In position space it is $\frac1{\nu_m}\sum_{\jmath}\varepsilon_{\jmath}\partial_{\jmath}(\bar{\tilde{Ξ}}\Sigma_{\imath\jmath}\tilde{Ξ})$, a total divergence of an antisymmetric bilinear, and in three dimensions the spatial indices of that bilinear pair into the spin three-vector. The bilinear $\bar{\tilde{Ξ}}\Sigma_{\imath\jmath}\tilde{Ξ}$ is the density whose integral is the spin of the state.

### The magnetic moment and $g=2$

Contract the spin term with the photon field. The interaction is $-\sum_{\imath}\varepsilon_{\imath} A_{\imath} j_{\imath}$, and the spin-dependent part contributes, up to a total divergence,

$$
-\frac{e}{4\pi\nu_m}\sum_{\imath,\jmath}\varepsilon_{\imath}\varepsilon_{\jmath}\,\partial_{\jmath}  A_{\imath}\,\bar{\tilde{Ξ}}\,\Sigma_{\jmath\imath}\tilde{Ξ}
= -\frac{e}{4\pi\nu_m}\cdot\tfrac12\sum_{\imath,\jmath}\varepsilon_{\imath}\varepsilon_{\jmath}\,F_{\imath\jmath}\,\bar{\tilde{Ξ}}\,\Sigma_{\imath\jmath}\tilde{Ξ},
$$

which is an effective **Pauli moment term**, of the form $-\frac{e}{2\,\nu_m}\vec B\cdot\vec S$ with $\vec S$ the spin density of the previous subsection. Its coefficient is the Dirac value $g=2$. The companion article on the anomalous magnetic moment writes the vertex as

$$
i\,e_{\imath}\,\cdot\,\vec e_{\mathrm{spt}(\imath)}\;F_1(k^2)+\frac{2i\sum_{\jmath}\varepsilon_{\jmath}\,\Sigma_{\imath\jmath}2\pi\nu_{\jmath}}{2m}\,F_2(k^2),
\qquad
g=2\big(1+F_2(0)\big),
$$

with $F_1(0)=1$ and $F_2(0)=0$ at tree level. The tree vertex is the generator alone; the Gordon identity rewrites that one structure as the sum of the convection and spin terms with equal coefficients, and that rewriting is the statement $g=2$. The anomaly is the part of the spin coefficient that the identity does not force, that is, the radiative correction to $F_2(0)$; the convection coefficient is protected by the Ward identity.

The same decomposition underlies the companion article on the classical origin of $g=2$: the factor of two is the statement that the spin-density gradient is twice as effective at generating an electric current as it is at contributing to the linear momentum, which is the factor-of-two asymmetry recorded below.

## The Massless Limit

The covariant identity needs $m\neq0$, because both terms carry $1/m$. A massless field has no mass to divide by, and the energy $E$ is the only scale available. The **structure** of the decomposition survives this step, and only the normalisation changes: one term is still a transport current, the other is still a total divergence.

Two statements can be made without a new derivation. The convection term, for a near plane wave of finite extent, is the charge transported at the group velocity, $e\rho\,2\pi\vec\nu_\Phi/E=e\rho\,\vec v$ with $\rho=j_0$ and $\vec v=2\pi\vec\nu_\Phi/E$; this reading uses only the density and the momentum, and it is the same in both regimes. The spin term is the divergence of the spin density, and in three dimensions the divergence of the antisymmetric pair of spatial indices is the curl of the spin three-vector,

$$
\vec S=\big(\bar{\tilde{Ξ}}\Sigma_{23}\tilde{Ξ},\;\bar{\tilde{Ξ}}\Sigma_{31}\tilde{Ξ},\;\bar{\tilde{Ξ}}\Sigma_{12}\tilde{Ξ}\big),
$$

so the spin term is a curl in the massless case exactly as it is in the massive one. What changes is the coefficient: $1/m$ in the massive identity, and $1/E$ in the massless regime, where $E$ is the only scale that can multiply a density to give a current.

For a massless particle of one value the spin is locked to the direction $\vec u_\Phi$ of the kinetic momentum, and the moment reads $\vec\mu=(e/E)(\frac{h\,\vec u_{\eta}}{4\pi})$: the massless limit removes the separation scale $m$ in favour of the energy $E$, and it does not remove the spin current. The rest-frame statement, where $E=m$ and the coefficient of the curl is $1/m$, is the one that fixes $g=2$, and it is the statement of the previous section.

## The Angular-Momentum and Stress-Tensor Relatives

The same split appears in the energy–momentum tensor, and the comparison is instructive because the numerical coefficients differ.

The symmetric **Belinfante–Rosenfeld** tensor is

$$
T_{\imath\jmath}^{\rm BR}
= -\frac14\Big(\bar{\tilde{Ξ}}\,e_{\imath}\,\partial_{\jmath}\tilde{Ξ}\,\vec e_{\mathrm{spt}(\imath)}
- \overline{\partial_{\jmath}\tilde{Ξ}}\,e_{\imath}\,\tilde{Ξ}\,\vec e_{\mathrm{spt}(\imath)}
+ \bar{\tilde{Ξ}}\,e_{\jmath}\,\partial_{\imath}\tilde{Ξ}\,\vec e_{\mathrm{spt}(\jmath)}
- \overline{\partial_{\imath}\tilde{Ξ}}\,e_{\jmath}\,\tilde{Ξ}\,\vec e_{\mathrm{spt}(\jmath)}\Big),
$$

where the coefficient is $-\frac14$ rather than $\frac{i}{4}$ because the two imaginary units of the conventional form multiply to $-1$, the one inside the generator and the one in front. On shell its time component is the energy density,

$$
T_{00}^{\rm BR}=\mathcal E=E\,j_0=E\,\operatorname{Sc}\big(\tilde{Ξ}^*\tilde{Ξ}\big),
$$

and its mixed components give the momentum density

$$
\vec P=\frac{1}{2i}\Big(\operatorname{Sc}\big(\tilde{Ξ}^*\vec\nabla_\Phi\tilde{Ξ}\big)-\operatorname{Sc}\big((\vec\nabla_\Phi\tilde{Ξ})^{*}\tilde{Ξ}\big)\Big)+\frac12\vec\nabla_\Phi\times\vec S .
$$

Compare this with the spin term of the Gordon identity: the spin contribution to the momentum density carries the coefficient $\tfrac12$, while the spin contribution to the electric current carries $1$. The spin-density gradient is therefore **twice as effective** at producing an electric current as at contributing to the linear momentum, and that factor of two is the Dirac value $g=2$ seen from the angular-momentum side.

The canonical (non-symmetric) tensor is the same expression with one pair of terms instead of two,

$$
T_{\imath\jmath}^{\rm canonical}
= -\frac12\Big(\bar{\tilde{Ξ}}\,e_{\imath}\,\partial_{\jmath}\tilde{Ξ}\,\vec e_{\mathrm{spt}(\imath)}
- \overline{\partial_{\jmath}\tilde{Ξ}}\,e_{\imath}\,\tilde{Ξ}\,\vec e_{\mathrm{spt}(\imath)}\Big),
$$

and it does not contain the bound spin-momentum term; that term is restored by the antisymmetric part of the Belinfante improvement. Integrating, the spin contribution to the total angular momentum is

$$
\int\vec r\times\big(\tfrac12\vec\nabla_\Phi\times\vec S\big)\,d^3r=\int\vec S\,d^3r,
$$

so the division by two is necessary for angular momentum and its absence is the statement of $g=2$ in the current.

### Spin in Maxwell's equations

The same strategy — split a conserved density into a transport part and a curl of a spin density — applies to light. For monochromatic Maxwell fields in the Riemann–Silberstein form, the time-averaged momentum density splits as $\vec P=\vec P_{\rm free}+\vec P_{\rm bound}$ with $\vec P_{\rm bound}=\tfrac12\vec\nabla_\Phi\times\vec S$, and the spin density can be identified, in the paraxial or pure-helicity case, with either $\vec S=\frac{\mu_0}{2i\omega}\vec H^{*}\times\vec H$ or $\vec S=\frac{\epsilon_0}{2i\omega}\vec E^{*}\times\vec E$; the two agree for a helicity state and may differ otherwise. This is the electromagnetic analogue of the Dirac decomposition, and the companion articles on the Riemann–Silberstein vector and on angular momentum and spin in biquaternionic form develop the same objects in the framework's notation.

## The Biquaternion Reading

### The split is central versus bivector

The one algebraic structure that the decomposition exhibits is the split of a product of two generators into its symmetric and antisymmetric parts: the **symmetric** part, one number per pair of indices, and in the algebra's terms the central direction; and the **bivector** part, antisymmetric, and in the algebra's terms the six directions $\vec e_\eta$ and $i\vec e_\eta$. The Gordon decomposition says that on shell the current splits in exactly this way. The convection term is the central direction, and the spin term is the bivector direction. This is the same identification the companion article on the anomalous magnetic moment records: the anomaly multiplies a bivector and is therefore an informational-sector object, while the tree-level convection term is central.

The comparison map of *Matrix Representations Conventions* reads the eight real units against the graded products of the algebra, and it sends the three vector units to the spacelike bivectors and the three imaginary units to the timelike ones. The **rotation-type** generators — the magnetic, spin-like ones, which are the timelike bivectors — sit therefore at the elements $i\vec e_\eta$, in the informational sector $\mathbb{B}_{\Psi}$, and the **boost-type** generators, the spacelike bivectors, at the vector units $\vec e_\eta$, in the material sector $\mathbb{B}_{\Phi}$. The frame of this article carries the right multiplier $\vec e_y$ in place of $e_t$, and that is a change of frame and not a change of the comparison map. The magnetic part of the Gordon split is therefore an $\mathbb{B}_{\Psi}$ structure, the same sector as the spin itself, and the convection part is the central direction. The sector labels are not decoration: they are the algebraic form of the statement that the convection term is the orbital transport and the spin term is the intrinsic moment.

### What the framework does not supply

The current is not a bilinear in the field and its conjugate alone. Written as a pairing it is a scalar part of three factors, $\tilde{Ξ}^*$, the generator, and the frame's unit $c_{\imath}$; and $c_{\imath}$ is not determined by the field. For the temporal component the unit cancels and the density is a scalar part of two factors; for the three spatial components it does not, and the unit $\vec e_z$ stands in the product. The older spelling puts the same datum in the adjoint, in a right multiplication that the field alone does not supply; the derived form of this article puts it in the last factor. Read from the operator side, as in the companion article on minimal coupling, the datum is a multiplication that the adjoint carries and the field does not. Either way the current needs one datum of the frame that the field does not carry, and that is the sense in which the framework does not derive this identity from a product inside the algebra. It transcribes the identity, names its two structures in the algebra's own sectors, and verifies the algebra of the split. The same caveat applies to the axial companion, which carries the chirality basis operator in addition to the frame's units.

What the algebra does supply is the location of the two terms: the convection term is the central direction, and the spin term is the bivector direction, with its magnetic part in the informational sector. That placement is a real bookkeeping statement, and it is the framework's contribution to this identity.

## Open Questions

1. **A current with no frame unit.** Is there an element of $\mathbb{B}$, built from the field and its conjugations alone, whose symmetric and antisymmetric parts reproduce the Gordon split without the unit $c_{\imath}$? This is the same question the minimal-coupling article leaves open for the current itself, and a positive answer here would be a positive answer there.

2. **The massless form.** In the massless case the spin term is a curl and the transport term is an energy-weighted derivative. Does the algebra, whose two values are carried by one element, write the massless decomposition more directly than the standard formulation does, and does it fix the locked moment of a one-valued field without going through the massive identity?

3. **The factor of two.** The $g=2$ asymmetry between the current and the momentum density is a mismatch between two coefficients of the same bivector, one in the current and one in the momentum density. Is there an algebraic statement that fixes the factor of two, or is it one more coefficient the algebra transcribes?

4. **The Belinfante improvement.** The passage from the canonical to the symmetric tensor is a shift by the divergence of an antisymmetric (spin) tensor. The corpus's Noether-theorem article gives the canonical currents; the form of the improvement term, and of the spin part of the angular momentum, is not written.

5. **The exact energy-normalised form.** The identity is proved for $m\neq0$, and the massless section replaces $m$ by $E$ as a matter of scale. Whether the decomposition can be written with $E$ in every coefficient, without passing through the massive form, is not settled here; the natural test is a stationary superposition, where the spin bilinear varies in space and the energy is common.

6. **Berry's spin for light.** The electromagnetic analogue identifies the intrinsic spin density with a curl of an $E$–$B$ cross product. The framework's field-strength biquaternion and its Riemann–Silberstein partner are the natural place to test whether this spin is the same object as the helicity of light in the framework.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *The AXF Matrices: Axis-Free, Integer Entries*, §*Why the Pauli and the Gamma Displays Are Refused*. The generators carry no frame label: $\gamma_{\imath}$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_\eta^2=-I_4$. The frame belongs to the coordinate, not to the array.

This section, and only this section, names the generator basis operators and the chirality basis operator by their standard Greek letters. Nothing above depends on the names: they are a change of typography for a reader who knows the Clifford notation, and every formula of the article is stated in the basis operator spelling.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}=a\tilde{Ξ}$ and $R_b\tilde{Ξ}=\tilde{Ξ} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad
\gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad
\gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad
\gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad
\gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad
\gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad
\gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad
\gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad
\gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

These are the basis operators of the conventions under their usual names: $\gamma_{\imath}$ is $iL_{\mathrm{pau},e_{\imath}}R_{\delta_{\imath}}$ and $\gamma_5$ is the chirality basis operator, so the dictionary between the two spellings is a subscript — $\delta_t=\vec e_x$ and $\delta_k=\vec e_y$ — together with a factor of $i$. In these names the relations read $\{\gamma_{\imath},\gamma_{\jmath}\}=2\varepsilon_{\imath}\delta_{\imath\jmath}$, $\gamma_{\imath}\gamma_{\jmath}=g_{\imath\jmath}-i\sigma_{\imath\jmath}$, $\{\gamma_{\imath},\gamma_5\}=0$, the equation $i\sum_{\imath}\varepsilon_{\imath}\gamma_{\imath}\nabla_{\imath}\tilde{Ξ}=2\pi\nu_m\tilde{Ξ}$, and the current $\tilde{Ξ}^{\dagger}iR_{\mathrm{axf},\vec e_x}\gamma_{\imath}\tilde{Ξ}$ with $\tilde{Ξ}^{\dagger}\gamma_0$. The mixed products of the proof are $\gamma_{\imath} L_{\mathrm{pau},e_{\jmath}}R_{\delta_{\jmath}}=-ig_{\imath\jmath}-\sigma_{\imath\jmath}$ and $L_{\mathrm{pau},e_{\jmath}}R_{\delta_{\jmath}}\gamma_{\imath}=-ig_{\imath\jmath}+\sigma_{\imath\jmath}$, and the axial vertex is $\gamma_{\imath}\gamma_5$, the product that the collapse $i\cdot(-i)=1$ writes as the real basis operator $L_{\mathrm{pau},e_{\imath}}R_{\delta_{\imath}}R_{\mathrm{pau},\vec e_z}$.

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

The reference-frame basis operator of the chirality operator is $\gamma_5$; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the basis operators span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_{\imath}}=C_{\Pi}L_{\mathrm{pau},e_{\imath}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a basis operator named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The Gordon decomposition splits the on-shell current of the field as

$$
\bar{\tilde{Ξ}}\,i\,e_{\imath}\,\tilde{Ξ}\,\vec e_{\mathrm{spt}(\imath)}
=\frac{i}{4\pi\nu_m}\Big(\bar{\tilde{Ξ}}\,\partial_{\imath}\tilde{Ξ}-\overline{\partial_{\imath}\tilde{Ξ}}\,\tilde{Ξ}\Big)
+\frac{1}{2\pi\nu_m}\sum_{\jmath}\varepsilon_{\jmath}\,\partial_{\jmath}\Big(\bar{\tilde{Ξ}}\,\Sigma_{\imath\jmath}\tilde{Ξ}\Big),
$$

into a convection part and the divergence of a spin density, $\Sigma_{\imath\jmath}$ being $i$ times the conventions' Lorentz generator, half the bivector of the pair. The field is an element of $\mathbb{B}$ and the current is a pairing, a scalar part of a product of elements whose last factor is the frame's unit $c_{\imath}$. In momentum space the same statement is

$$
\bar w_2\,i\,e_{\imath}\,w\,\vec e_{\mathrm{spt}(\imath)}
= \frac{(p+p_2)_{\imath}}{2\,m\,c}\,\bar w_2w
+ \frac{i}{m\,c}\sum_{\jmath}\varepsilon_{\jmath}\,(p_2-p)_{\jmath}\,\bar w_2\Sigma_{\imath\jmath}w,
$$

where the first term is the current of a charged scalar and the second is the spin term whose coefficient gives $g=2$. The decomposition requires $m\neq0$ because both terms carry $1/m$; in the massless regime the energy $E$ replaces the mass as the scale of both terms, the spin term remains the curl of the spin density, and the locked moment of a one-valued field is what remains of the Dirac moment when the rest frame is lost. The Belinfante–Rosenfeld tensor contains the same spin term with coefficient $\tfrac12$ in the momentum density, and the mismatch between that $\tfrac12$ and the current's $1$ is the angular-momentum face of $g=2$. The axial companion is the same parent identity at the real action $e_{\imath}\cdot\vec e_z\vec e_{\mathrm{spt}(\imath)}$, and there the transfer and the average momentum exchange their slots.

The biquaternion interpretation is a naming of the two structures: the split of the generator product is the split into its central part and its bivector part, so the convection current is central and the spin current is a bivector whose rotation-type part lies in the informational sector $\mathbb{B}_{\Psi}$ and whose boost-type part lies in $\mathbb{B}_{\Phi}$. The identity is not a bilinear in the field and its conjugate alone; the current carries one unit of the frame that the field does not carry, and that is the datum the framework transcribes rather than derives.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{Ξ}$, $\tilde{Ξ}_{L}$, $\tilde{Ξ}_{R}$ | The field, an element of $\mathbb{B}$; the value is the subscript, $L$ the minus one and $R$ the plus one |
| $e_{\imath}$, $\varepsilon_{\imath}$, $\delta_{\imath\jmath}$ | The four units, $e_t$ and $\vec e_\eta$; the plain weight of the conventions, and the Kronecker delta |
| $\vec e_{\mathrm{spt}(\imath)}$ | The frame's right multipliers, with $\mathrm{spt}(t)=x$ and $\mathrm{spt}(\eta)=y$ |
| $ie_{\imath}\,\cdot\,\vec e_{\mathrm{spt}(\imath)}$, the action $\tilde Q\mapsto ie_{\imath}\tilde Q\vec e_{\mathrm{spt}(\imath)}$ | The four generators of the frame; each exchanges the value |
| $-i\,\cdot\,\vec e_z$, the action $\tilde Q\mapsto-i\tilde Q\vec e_z$ | The chirality basis operator, named once; it keeps the value |
| $\bar{\tilde{Ξ}}\,X=\operatorname{Sc}(\tilde{Ξ}^*iX\vec e_x)$ | The pairing: a scalar part of a product of elements; a derived form of this article |
| $c_{\imath}$ | The frame's unit in the current, $c_t=e_t$ and $c_k=\vec e_z$ |
| $\Sigma_{\imath\jmath}$ | The spin generator, $\frac{i}{4}$ times the commutator of the two generators, antisymmetric; $i$ times the Lorentz generator of the conventions, which is half the bivector of the pair |
| $\sum_{\imath}\varepsilon_{\imath} e_{\imath}\partial_{\imath}\tilde{Ξ}\,\vec e_{\mathrm{spt}(\imath)}=-2\pi\nu_m\tilde{Ξ}$ | The field equation, every factor written out |
| $\sum_{\imath}\varepsilon_{\imath}\overline{\partial_{\imath}\tilde{Ξ}}\,e_{\imath} X\vec e_{\mathrm{spt}(\imath)}=m\bar{\tilde{Ξ}}X$ | The adjoint equation, for every element $X$; the mass carries the other sign |
| $\tilde\nabla_\Phi\tilde{Ξ}_{R}=2\pi\nu_m\tilde{Ξ}_{L}$, $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=2\pi\nu_m\tilde{Ξ}_{R}$ | The chiral pair, the same operator content by left multiplication |
| $j_{\imath}=\bar{\tilde{Ξ}}\,ie_{\imath}\tilde{Ξ}\vec e_{\mathrm{spt}(\imath)}=\operatorname{Sc}(\tilde{Ξ}^*e_{\imath}\tilde{Ξ} c_{\imath})$, $j_0=\operatorname{Sc}(\tilde{Ξ}^*\tilde{Ξ})$ | The number current and its density |
| $p$, $p_2$, $2\pi\nu_{\jmath}=(p_2-p)_{\jmath}$, $P_{\imath}=\tfrac12(p+p_2)_{\imath}$ | Momenta, transfer and average |
| $\bar w_2\,ie_{\imath} w\,\vec e_{\mathrm{spt}(\imath)}$ | The momentum-space bilinear |
| $a$, $b$ | The two multipliers of the parent identity |
| $e_{\imath}\,\cdot\,\vec e_z\vec e_{\mathrm{spt}(\imath)}$ | The axial vertex, a real action |
| $\vec S=(\bar{\tilde{Ξ}}\Sigma_{23}\tilde{Ξ},\bar{\tilde{Ξ}}\Sigma_{31}\tilde{Ξ},\bar{\tilde{Ξ}}\Sigma_{12}\tilde{Ξ})$ | The spin density three-vector |
| $T_{\imath\jmath}^{\rm BR}$, $T_{\imath\jmath}^{\rm canonical}$ | The Belinfante–Rosenfeld and canonical stress tensors |
| $\frac{e}{2\,\nu_m}\cdot\frac12\sum_{\imath,\jmath}\varepsilon_{\imath}\varepsilon_{\jmath} F_{\imath\jmath}\bar{\tilde{Ξ}}\Sigma_{\imath\jmath}\tilde{Ξ}$ | The effective Pauli moment term, $g=2$ |

## Further Reading

- [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html#why-the-pauli-and-the-gamma-displays-are-refused), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- W. Gordon, "Der Comptoneffekt nach der Schrödingerschen Theorie," *Zeitschrift für Physik* **40** (1926) 117–133, for the origin of the current decomposition.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the Gordon decomposition, the bilinears and the $1/2m$ coefficient of the spin current.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the vertex decomposition into $F_1$ and $F_2$, the Gordon identity and the Ward identity.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the form factors, the Gordon decomposition and the renormalisation of the vertex.
- L. H. Ryder, *Quantum Field Theory* (Cambridge, 2nd ed. 1996), for the Gordon decomposition and its use in the magnetic moment.
- M. V. Berry, "Optical currents," *Journal of Optics A: Pure and Applied Optics* **11** (2009) 094001, for the Gordon strategy applied to Maxwell's equations and the intrinsic spin density of light.
- F. J. Belinfante, "On the spin angular momentum of mesons," *Physica* **6** (1939) 887–898, and L. Rosenfeld, "Sur le tenseur d'impulsion-énergie," *Mémoires de l'Académie Royale de Belgique* **18** (1940) 1–30, for the symmetric stress tensor and the spin improvement.
- The companion articles of this series: [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html), [The Anomalous Magnetic Moment in Biquaternionic Form](the-anomalous-magnetic-moment-in-biquaternionic-form.html), [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), *The Classical Origin of $g = 2$ in Biquaternionic Form*, and [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html).
