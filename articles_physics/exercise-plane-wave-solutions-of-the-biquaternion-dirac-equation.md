# __Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation__

## Introduction

This is a worked exercise on the biquaternion Dirac equation, written in the biquaternion algebra and on its elements. The field is one biquaternion, the derivative is the corpus gradient $\tilde\nabla$, and every result below is a statement about elements and their products. The parent article, *The Biquaternion Dirac Equation — Solutions and the Non-Relativistic Limit*, supplies the equation, the field, the two frequency branches and the mass shell. The present exercise re-derives the parent's results in the algebra and supplies what the parent leaves implicit: the solutions written as elements, the normalisation in the biquaternion pairing, the spin sums as products of elements, the massless limit, the change of the reading of the two parts, and the helicity pieces with their determinant.

**One operator, two members.** The gradient is the one first-order operator of the equation, and the mass couples two members,

$$
\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=m\tilde{Ξ}^{\mathrm{sp}}_L,\qquad \tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=m\tilde{Ξ}^{\mathrm{sp}}_R ,
$$

which is the dynamics of *Operator and Calculus Conventions*, §*The Gradient*. Each member is first order and each acts from the left. The gradient is a left multiplication, so it acts inside one part; the mass term is the only term that names the other part, and it is the only coupling between the two. The free equation keeps one member and one field, $\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}=0$. The massive equation is the pair and not a one-field equation of first order, because $\tilde\nabla^2$ is not a scalar: the scalar second-order operator of the algebra is $\Box=\tilde\nabla\tilde\nabla^{\natural}$, and only that product is the wave operator.

**The two parts.** The field carries the chirality subscript of *Special Element Conventions*, §*The Chirality Convention*, and its two parts are read by the right action $\tilde Q\mapsto-i\tilde Q\vec e_z$: the value $-1$ written $L$ and the value $+1$ written $R$. A left multiplication keeps the value, a product takes the value of its right factor, a scalar multiple keeps the value, and a right multiplication by $\vec e_x$ or by $\vec e_y$ exchanges the two values. The gradient multiplies on the left and the reading on the right, so no derivative moves a part from one value to the other; the mass term, which names the other part, is the only term that does.

**The seven problems** are: **(1)** the solutions at rest and at general momentum; **(2)** the covariant normalisation and the orthogonality; **(3)** the spin sums; **(4)** the massless limit and the locking of helicity to the member; **(5)** the two parts and the change of the reading; **(6)** the biquaternionic mass shell; **(7)** the helicity pieces and the piece determinant. Problems 1, 2, 4 and 6 use the action on elements, Problems 3 and 7 the wave element read with it, and Problem 5 the two parts themselves.

## The Gradient and the Two Parts

**The gradient.** It is the element-valued operator of *Operator and Calculus Conventions*, §*The Gradient*, and it is written out here once, because the exercise uses no other derivative:

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial Q_\mu}
=e_t\frac{\partial}{\partial Q_t}+\vec e_x\frac{\partial}{\partial Q_x}+\vec e_y\frac{\partial}{\partial Q_y}+\vec e_z\frac{\partial}{\partial Q_z},
$$

with its quaternion conjugate and the d'Alembertian,

$$
\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu}
=e_t\frac{\partial}{\partial Q_t}-\vec e_x\frac{\partial}{\partial Q_x}-\vec e_y\frac{\partial}{\partial Q_y}-\vec e_z\frac{\partial}{\partial Q_z},
\qquad \varepsilon=(1,-1,-1,-1),
$$

$$
\Box=\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q ,
\qquad \Delta_Q=\frac{\partial^2}{\partial Q_x^2}+\frac{\partial^2}{\partial Q_y^2}+\frac{\partial^2}{\partial Q_z^2}.
$$

On the material sector $Q_t=i c r'_t$ the time derivative is $\partial/\partial Q_t=-(i/c)\,\partial/\partial t'$ and the d'Alembertian is $\Delta-c^{-2}\partial^2/\partial{r'_{t}}^2$. These lines are the whole operator content of the exercise, and no letter other than $\tilde\nabla$ names the gradient.

**The square of the gradient is not scalar.** The product $\tilde\nabla\tilde\nabla$ is

$$
\tilde\nabla^2=\frac{\partial^2}{\partial Q_t^2}-\Delta_Q+2\sum_k\vec e_k\frac{\partial^2}{\partial Q_t\partial Q_k},
$$

because $e_t$ commutes with the three spatial units while the spatial units anticommute among themselves. The mixed terms are the ones the conjugate removes: in $\tilde\nabla\tilde\nabla^{\natural}$ the coefficient of $\partial^2/\partial Q_t\partial Q_k$ is $e_te_k-\vec e_ke_t=0$, and the coefficient of $\partial^2/\partial Q_\mu^2$ is $\varepsilon_\mu e_\mu^2=1$. So the equation is the pair: the square with the conjugate is the scalar $\Box$ and the square with itself is not a scalar, so no single first-order equation on one field can carry a mass term.

**The wave element.** A plane wave is $\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}}_0\exp(i\theta)$ with $\theta=\vec k\cdot(r_x\vec e_x+r_y\vec e_y+r_z\vec e_z)-\omega t'$, its polarisation $\tilde{Ξ}^{\mathrm{sp}}_0$ an element that does not depend on the coordinates. The phase is central, so it commutes with the polarisation, and the gradient differentiates it to left multiplication by

$$
i\tilde P=-\tilde K,\qquad
\tilde P=i k_0e_t+k_1\vec e_x+k_2\vec e_y+k_3\vec e_z,\qquad
\tilde K=k_0-i\vec k,
$$

with $k_0=\omega$ and $\vec k=k_1\vec e_x+k_2\vec e_y+k_3\vec e_z$; in natural units $k_0=E$ and $\vec k=\vec p$. The wave element is that of the material sector, imaginary scalar part and real vector part, and its two scalar squares are

$$
\tilde K^{\natural}\tilde K=k_0^2-\lvert\vec k\rvert^2=p^2,\qquad
\tilde P\tilde P^{\natural}=-p^2,\qquad p^2=k_0^2-\lvert\vec k\rvert^2 .
$$

Each line is one use of $i^2=-1$ and one use of $\vec k^{\,2}=-\lvert\vec k\rvert^2$, and the two lines agree because $\tilde K=-i\tilde P$. The symbol of the free equation is the left multiplication by $-\tilde K$, that is by $i\tilde P$: the gradient and the wave element are the same object read twice. The two squares vanish together exactly when $p^2=0$, and that is the null wave element of Problem 4, where the symbol loses rank and the solutions of the free equation become the kernel.

**The two parts.** The value of an element is read by the right action $\tilde Q\mapsto-i\tilde Q\vec e_z$. The action applied twice returns the element, so its spectrum is $+1,+1,-1,-1$: two values, of two complex dimensions each. A basis of the part of value $+1$ is

$$
e_t-i\vec e_z,\qquad \vec e_x+i\vec e_y,
$$

and a basis of the part of value $-1$ is $e_t+i\vec e_z$, $\vec e_x-i\vec e_y$. Three facts are used below and no fourth: a left multiplication keeps the value, a product takes the value of its right factor, and a right multiplication by $\vec e_x$ or by $\vec e_y$ exchanges the two values. The last is a property of the four units and not of an element, it is what the pairing of Problem 2 uses, and it is what the gradient never does.

**The change of the reading.** The value can be read on another unit. Let $\tilde Q_{\mathrm{disp}}=(e_t+\vec e_y)/\sqrt2$, a unit element with $\tilde Q_{\mathrm{disp}}^{-1}=\tilde Q_{\mathrm{disp}}^{\natural}=(e_t-\vec e_y)/\sqrt2$. Conjugation by it fixes the spatial unit $\vec e_y$ and carries the other two into one another,

$$
\tilde Q_{\mathrm{disp}}^{-1}(i\vec e_x)\tilde Q_{\mathrm{disp}}=i\vec e_z,\qquad
\tilde Q_{\mathrm{disp}}^{-1}(-i\vec e_z)\tilde Q_{\mathrm{disp}}=i\vec e_x,\qquad
\tilde Q_{\mathrm{disp}}^{-1}\vec e_y\tilde Q_{\mathrm{disp}}=\vec e_y .
$$

Right multiplication of the field by $\tilde Q_{\mathrm{disp}}$ therefore moves the reading from $\vec e_z$ to $\vec e_x$: for $\tilde{Ξ}=\tilde{Ξ}^{\mathrm{sp}}\tilde Q_{\mathrm{disp}}$ the identity $\tilde Q_{\mathrm{disp}}\vec e_x=\vec e_z\tilde Q_{\mathrm{disp}}$ gives

$$
-i\tilde{Ξ}\vec e_x=(-i\tilde{Ξ}^{\mathrm{sp}}\vec e_z)\tilde Q_{\mathrm{disp}},
$$

so the value read on $\vec e_x$ after the change is the value read on $\vec e_z$ before it. The change is a right multiplication and every derivative is a left multiplication, so it commutes with $\tilde\nabla$: the change of the reading moves the labels and touches no derivative.

## The Field and the Equation

**The field.** The field is one element $\tilde{Ξ}^{\mathrm{sp}}$ of $\mathbb B$ with its two parts $\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}}_L+\tilde{Ξ}^{\mathrm{sp}}_R$ (§*The Chirality Convention*). Nothing further is needed to state the field: the two parts are the two values of one element, and the field is the element itself.

**The equation.** For a plane wave of four-momentum $(E,\vec p)$ the two members become the momentum-space system

$$
i\tilde P\,\tilde{Ξ}^{\mathrm{sp}}_R=m\,\tilde{Ξ}^{\mathrm{sp}}_L,\qquad i\tilde P^{\natural}\,\tilde{Ξ}^{\mathrm{sp}}_L=m\,\tilde{Ξ}^{\mathrm{sp}}_R ,
$$

one equation on each part, and the two are one statement: the second is the first with the gradient replaced by its conjugate and the two parts exchanged, so the mass stands with the same sign on both sides. Eliminating the second part gives

$$
\tilde P^{\natural}\tilde P\,\tilde{Ξ}^{\mathrm{sp}}_R=-m^2\tilde{Ξ}^{\mathrm{sp}}_R ,
$$

which is the mass shell of Problem 6 and the Klein–Gordon equation of the first part.

**Conventions.** Natural units $\hbar=c=1$ in the solutions; $\hbar$ and $c$ are restored in Problem 6. The frame is the $\mathbb{M}_-$ frame of *Frame and Metric Conventions*, §*The $\mathbb{M}_-$ Frame*, and the values are read on its third direction, $\vec e_z$. The helicity direction is $\vec u_p=\vec p/\lvert\vec p\rvert$, and the helicity element is $\tilde{Ζ}=i\vec u_p$, a root of the central value $+1$, $\tilde{Ζ}^2=e_t$. The Hermitian conjugation $^{*}$ is the one of *Algebra and Element Conventions*, §*The Conjugations*, and the contraction of the gradient with a momentum is written out rather than slashed, as *Index Notation and Corpus Conventions* requires: hence the element $i\tilde P$ for the symbol and no slash anywhere in the article.

## Problem 1: The solutions at rest and at general momentum

**Statement.** Solve the pair for the positive-frequency branch $\tilde w$ and for the negative-frequency branch $\tilde v$, explicitly at rest and at general momentum, in the two readings.

**Solution.** Eliminating the second part gives $\tilde\nabla^{\natural}\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=\Box\tilde{Ξ}^{\mathrm{sp}}_R=m^2\tilde{Ξ}^{\mathrm{sp}}_R$; on a plane wave $\Box$ is $p^2$, so the pair is soluble exactly on the mass shell

$$
E^2=\vec p^{\,2}+m^2 .
$$

On the shell the second part is free and the first is determined by the gradient:

$$
\boxed{\;\tilde{Ξ}^{\mathrm{sp}}_L=\frac1m\,\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=\frac{i}{m}\,\tilde P\,\tilde{Ξ}^{\mathrm{sp}}_R\;}
$$

The part $\tilde{Ξ}^{\mathrm{sp}}_R$ is two-complex-dimensional, so the space of positive-frequency solutions at fixed momentum is two-dimensional, and it carries no further label. The label is the helicity, and it is the two values of the helicity element: left multiplication by $\tilde{Ζ}$ commutes with left multiplication by $\tilde P$, as it does with every left multiplication by an element that commutes with $\tilde{Ζ}$, so its two eigenspaces cut the space into two one-dimensional pieces, one for each value.

**The amplitudes.** Along a helicity eigenstate the two parts have unequal size, and the ratio is fixed. Writing $\langle\tilde Q\rangle_{*}$ for the Hermitian norm,

$$
\frac{\langle\tilde{Ξ}^{\mathrm{sp}}_L\rangle_{*}}{\langle\tilde{Ξ}^{\mathrm{sp}}_R\rangle_{*}}=\frac{E\mp\lvert\vec p\rvert}{E\pm\lvert\vec p\rvert},
$$

with the upper sign for helicity $+1$ and the lower for helicity $-1$: the left part dominates for the negative helicity and the right part for the positive one, and at the massless point one of the two vanishes. The squared amplitudes are the two factors whose product is $m^2$, and that product is what makes the covariant normalisation of Problem 2 come out at $2m$.

**The negative-frequency branch.** The same construction with $m$ replaced by $-m$:

$$
\boxed{\;\tilde v_L=-\frac1m\,\tilde\nabla\tilde v_R=-\frac{i}{m}\,\tilde P\,\tilde v_R\;}
$$

so that the pair holds with the sign of the mass reversed. The two branches together give the two frequency signs, and the two helicity values within each branch give the four-dimensional complex solution space of the parent.

**At rest.** With $\vec p=0$ and $E=m$ the wave element is $\tilde P=ime_t$, the gradient acts on the phase as the central element $-m$, and the pair reads

$$
-m\,\tilde w_R(0)=m\,\tilde w_L(0),\qquad -m\,\tilde w_L(0)=m\,\tilde w_R(0),
$$

that is $\tilde w_L(0)=-\tilde w_R(0)$, with the sign reversed for the negative-frequency branch. Each solution space is two-dimensional over $\mathbb C$, the two dimensions of the part of value $R$, and a basis of the positive-frequency space is

$$
e_t-i\vec e_z,\qquad \vec e_x+i\vec e_y,
$$

with the two signs exchanged for the negative-frequency space. The rest frame supplies no direction to the operator: at $\vec p=0$ the gradient is $e_t\,\partial/\partial Q_t$ alone and its symbol is a central scalar, so the two dimensions are the two dimensions of the part and not two directions of a spin. The axis enters through the reading, as in the next paragraph.

**The other reading.** Right multiplication by $\tilde Q_{\mathrm{disp}}$ carries a solution of one reading to a solution of the other, because the change of the reading touches no derivative: if the pair holds for $\tilde{Ξ}^{\mathrm{sp}}$, then right multiplication by the unit element carries it to a pair that holds for $\tilde{Ξ}^{\mathrm{sp}}\tilde Q_{\mathrm{disp}}$. In that reading the unit on which the value is read is $\vec e_x$, whose part of value $+1$ has the basis

$$
e_t-i\vec e_x,\qquad \vec e_z+i\vec e_y ,
$$

and the rest solutions are the same elements with the reading moved. The two parts are mixed again as soon as the momentum is not zero.

## Problem 2: Covariant normalisation and orthogonality

**Statement.** Verify $\langle\tilde w,\tilde w\rangle_{\mathrm D}=2m$, $\langle\tilde v,\tilde v\rangle_{\mathrm D}=-2m$, $\langle\tilde w,\tilde v\rangle_{\mathrm D}=0$, and the Hermitian products.

**Solution.** The Dirac pairing is the Hermitian one twisted by the timelike unit,

$$
\langle\tilde{Ξ}^{\mathrm{sp}},\tilde{Ξ}\rangle_{\mathrm D}=\mathrm{Tr}\bigl(\tilde{Ξ}^{\mathrm{sp}*}\tilde{Ξ}\,i\vec e_x\bigr),
$$

the pairing of the parent, with the trace of *Norm and Unitary Conventions*. The twist is the time direction of the frame, and it is what makes the pairing a Lorentz scalar; the twist exchanges the two values, so the pairing couples the two parts crossed, $\tilde{Ξ}^{\mathrm{sp}}_L$ with $\tilde{Ξ}_R$ and $\tilde{Ξ}^{\mathrm{sp}}_R$ with $\tilde{Ξ}_L$, and the two diagonal terms vanish in the trace, so only the crossed terms remain. The single algebraic input of the section is the unit-vector identity

$$
(i\vec u_p)^2=i^2\,\vec u_p^{\,2}=(-1)(-e_t)=e_t,
$$

the biquaternion form of the statement that a unit direction squares to $-1$ up to the two minus signs, which cancel.

**The four values.** For the positive-frequency solution the pairing is twice the geometric mean of the two amplitude norms, $\sqrt{E\mp\lvert\vec p\rvert}\,\sqrt{E\pm\lvert\vec p\rvert}=\sqrt{E^2-\vec p^{\,2}}=m$, so

$$
\langle\tilde w_\pm,\tilde w_\pm\rangle_{\mathrm D}=2m .
$$

For the negative-frequency branch the left part carries the minus sign of Problem 1 and the same computation gives $-2m$:

$$
\langle\tilde v_\pm,\tilde v_\pm\rangle_{\mathrm D}=-2m .
$$

The mixed term vanishes because the two products are opposite and cancel:

$$
\langle\tilde w_\pm,\tilde v_\pm\rangle_{\mathrm D}=0,
$$

and opposite helicities are orthogonal for the same reason, $\langle\tilde w_+,\tilde w_-\rangle_{\mathrm D}=0$, since the two right parts are eigenvectors of $\tilde{Ζ}$ with opposite values.

**The Hermitian products.** The untwisted product is the positive one and does not cancel:

$$
\mathrm{Tr}\bigl(\tilde w_\pm^{*}\tilde w_\pm\bigr)=(E\mp\lvert\vec p\rvert)+(E\pm\lvert\vec p\rvert)=2E,\qquad
\mathrm{Tr}\bigl(\tilde v_\pm^{*}\tilde v_\pm\bigr)=2E .
$$

The bilinear is a Lorentz scalar and its value $2m$ is the covariant normalisation; it is not the probability density, which is the positive quantity $\mathrm{Tr}(\tilde w^{*}\tilde w)=2E$. As a numerical check, for $m=1$ and $\lvert\vec p\rvert=0.6$, hence $E=1.166190$, direct evaluation gives $\langle\tilde w,\tilde w\rangle_{\mathrm D}=2.0000$, $\langle\tilde v,\tilde v\rangle_{\mathrm D}=-2.0000$, $\langle\tilde w,\tilde v\rangle_{\mathrm D}=0$, and $\mathrm{Tr}(\tilde w^{*}\tilde w)=\mathrm{Tr}(\tilde v^{*}\tilde v)=2.3324=2E$.

## Problem 3: The spin sums

**Statement.** Verify that for every element $\tilde{Ξ}$,

$$
\sum_{\pm}\tilde w_\pm\,\langle\tilde w_\pm,\tilde{Ξ}\rangle_{\mathrm D}=i\tilde P\,\tilde{Ξ}+m\,\tilde{Ξ},\qquad
\sum_{\pm}\tilde v_\pm\,\langle\tilde v_\pm,\tilde{Ξ}\rangle_{\mathrm D}=i\tilde P\,\tilde{Ξ}-m\,\tilde{Ξ} .
$$

**Solution.** The left-hand side is a sum of two products of elements, one per helicity, and read as an operator it has rank two: each term is the solution multiplied by the number its pairing with $\tilde{Ξ}$ returns. The two solutions at fixed momentum are the two helicity eigenstates, and their parts $\tilde{Ξ}^{\mathrm{sp}}_R$ span the part of value $R$, so the sum reproduces $\tilde{Ξ}$ on the right and, through the action, on the left. The right-hand side is the element $i\tilde P+m$ multiplying $\tilde{Ξ}$ on the left, which is the gradient plus the mass read on a plane wave of the momentum: $\tilde\nabla\tilde{Ξ}+m\tilde{Ξ}$. The negative-frequency sum is identical in structure with the roles of the two values interchanged, and gives the gradient minus the mass. Both hold for every element and not only on the solutions, and both were checked on a basis of $\mathbb B$.

**The second-order closure.** The two sums are complementary, and eliminating between the members gives the closure

$$
\tilde\nabla^{\natural}\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=\Box\tilde{Ξ}^{\mathrm{sp}}_R=m^2\tilde{Ξ}^{\mathrm{sp}}_R .
$$

The scalar square is the interval, and the collapse is two lines:

$$
\tilde K^{\natural}\tilde K=k_0^2-k_0i\vec k+i\vec kk_0-i^2\vec k^{\,2}=k_0^2+\vec k^{\,2}=k_0^2-\lvert\vec k\rvert^2=p^2,
$$

with the cross terms vanishing because $k_0$ is central and $\vec k$ is pure, and with the plus in front of $\vec k^{\,2}$ because the square of $i\vec k$ is $i^2\vec k^{\,2}=+\lvert\vec k\rvert^2$. On the mass shell $\tilde P^{\natural}\tilde P=-m^2$, so $\Box=m^2$ on the wave and the pair closes; the two branches then close the solution space, and no third condition is needed.

**No trace enters.** Each of the two sums is a product of elements and a scalar, and each of the two members is a left multiplication by an element. Neither line needs a trace, a basis or an index: the identity is an identity of the algebra, and the rank-two reading of its left side is the statement that the two helicity solutions span the part of value $R$.

## Problem 4: The massless limit and the locking of helicity to the member

**Statement.** Take $m=0$ and exhibit the locking of helicity to the member.

**Solution.** At $m=0$ the mass term is gone and the pair decouples into two independent equations, one on each part:

$$
\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=0,\qquad \tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=0 .
$$

For $m=0$ the dispersion is $E=\lvert\vec p\rvert$ and the wave element is null, $\tilde P\tilde P^{\natural}=0$, so the left multiplication by $\tilde P$ loses rank and its kernel is of two complex dimensions. Every element of that kernel carries helicity $+1$:

$$
\tilde P\,\tilde F=0\ \Longrightarrow\ \tilde{Ζ}\,\tilde F=+\tilde F,\qquad
\tilde P^{\natural}\,\tilde F=0\ \Longrightarrow\ \tilde{Ζ}\,\tilde F=-\tilde F .
$$

So the labels are locked to the members: **the field annihilated by $\tilde\nabla$ carries positive helicity and the field annihilated by $\tilde\nabla^{\natural}$ negative helicity.** The mass is the only term that couples the two members, and setting it to zero decouples them; the two kernels are of two complex dimensions each and meet only at zero, so together they account for the four complex dimensions of the carrier.

**The position-space reading.** On the material sector the free member reads

$$
-\frac{i}{c}\,e_t\frac{\partial\tilde{Ξ}^{\mathrm{sp}}}{\partial t'}+\sum_k\vec e_k\frac{\partial\tilde{Ξ}^{\mathrm{sp}}}{\partial Q_k}=0 .
$$

In natural units the same line is read for $\partial\tilde{Ξ}^{\mathrm{sp}}/\partial t'$: with $c=1$,

$$
\frac{\partial\tilde{Ξ}^{\mathrm{sp}}}{\partial t'}=-i\sum_k\vec e_k\frac{\partial\tilde{Ξ}^{\mathrm{sp}}}{\partial Q_k},
$$

one equation on the element, whose two solutions are the two locked states above. The magnitude $\lvert\vec p\rvert$, which the energy carries at $m=0$, is part of the right-hand side and cannot be dropped.

## Problem 5: The two parts and the change of the reading

**Statement.** Verify the two values, the two bases, and the effect of the change of the reading.

**Solution.** The value is read by the right action $\tilde Q\mapsto-i\tilde Q\vec e_z$, and it is an action of the algebra and not a derivative: it depends on the frame's third direction and on nothing else. Applied twice it returns the element,

$$
-i\bigl(-i\tilde Q\vec e_z\bigr)\vec e_z=\tilde Q\vec e_z\vec e_z=\tilde Q ,
$$

so its spectrum is $+1,+1,-1,-1$ and the part of value $+1$, written $\tilde Q_R$, is of two complex dimensions. The two bases of the section *The Gradient and the Two Parts* are one line each to check: $f\vec e_z=if$ for $e_t-i\vec e_z$ and for $\vec e_x+i\vec e_y$, and $f\vec e_z=-if$ for $e_t+i\vec e_z$ and for $\vec e_x-i\vec e_y$.

**The action on the two parts.** A left multiplication keeps the value, because the reading multiplies on the right and the two sides commute; a right multiplication by $\vec e_x$ or by $\vec e_y$ exchanges the two values, because those two units anticommute with $\vec e_z$; a product takes the value of its right factor. Write $\mathbb B_L$ and $\mathbb B_R$ for the two parts, the elements of value $-1$ and of value $+1$. Then

$$
\tilde{Ζ}\,\tilde Q_L\in\mathbb B_L,\qquad
\tilde Q_L\,\vec e_x\in\mathbb B_R,\qquad
\tilde Q_R\,\vec e_y\in\mathbb B_L,
$$

the first because a left multiplication keeps the value, the second and the third because the two spatial units anticommute with $\vec e_z$. These are the three facts the whole exercise rests on, and they are read from the multiplication table of the four units.

**The change of the reading.** Right multiplication by $\tilde Q_{\mathrm{disp}}=(e_t+\vec e_y)/\sqrt2$ is a unit element, and it moves the reading from $\vec e_z$ to $\vec e_x$:

$$
\tilde{Ξ}^{\mathrm{sp}}_d=\tilde{Ξ}^{\mathrm{sp}}_c\,\tilde Q_{\mathrm{disp}},\qquad
-i\tilde{Ξ}^{\mathrm{sp}}_d\vec e_x=(-i\tilde{Ξ}^{\mathrm{sp}}_c\vec e_z)\tilde Q_{\mathrm{disp}} .
$$

The two values are unchanged, the two bases move with the reading, and no derivative changes: a left multiplication passes through a right multiplication, so $\tilde\nabla$ applied before or after the change gives the same result. The change is a right multiplication of the element and not a linear map of something other than the element: it moves the reading, and the element is the same element.

## Problem 6: The biquaternionic mass-shell condition

**Statement.** Verify the mass-shell condition of the parent and recover the relativistic energy–momentum relation.

**Solution.** The plane-wave ansatz carries the wave biquaternion

$$
\tilde P/\hbar=\frac{i\omega}{c}\,e_t+\vec k,\qquad \vec k=k_1\vec e_x+k_2\vec e_y+k_3\vec e_z ,
$$

an element of the material sector $\mathbb{M}_-$: imaginary scalar part and real vector part. Its quaternionic norm is the norm of *Algebra and Element Conventions*, §*The Conjugations*, so

$$
\langle\tilde P/\hbar\rangle_{\natural}=\left(\frac{i\omega}{c}\right)^2+k_1^2+k_2^2+k_3^2=-\frac{\omega^2}{c^2}+\vec k^2 ,
$$

the sign change being $i^2=-1$. The dispersion relation is $\omega^2=c^2\vec k^2+m^2c^4/\hbar^2$, and substituting it,

$$
\langle\tilde P/\hbar\rangle_{\natural}=-\frac{1}{c^2}\left(c^2\vec k^2+\frac{m^2c^4}{\hbar^2}\right)+\vec k^2=-\frac{m^2c^2}{\hbar^2},
$$

which is the parent's condition

$$
\boxed{\;\tilde P\tilde P^{\natural}=-m^2c^2\;}.
$$

Equivalently, with $E=\hbar\omega$ and $\vec p=\hbar\vec k$, the norm is quadratic, so $\langle\tilde P/\hbar\rangle_{\natural}=\langle\tilde P\rangle_{\natural}/\hbar^2=-m^2c^2/\hbar^2$. The mass shell is not a new postulate: it is the statement that the four-wavevector is a timelike element of $\mathbb{M}_-$ with the same quaternionic norm as the four-momentum.

The two roots $\omega=\pm\sqrt{c^2\vec k^2+m^2c^4/\hbar^2}$ are the two frequency branches, and they are the two families $\tilde w$ and $\tilde v$ constructed above; the two helicity values within each branch give the four-dimensional complex solution space. As a numerical check, for an electron ($mc^2=0.510998950\ \mathrm{MeV}$) at $\lvert\vec p\rvert=1\ \mathrm{MeV}/c$, the dispersion gives $E=1.122996\ \mathrm{MeV}$ and $E^2-\vec p^2c^2=0.261120\ \mathrm{MeV}^2=(mc^2)^2$; the wave biquaternion has $\langle\tilde P/\hbar\rangle_{\natural}=-6.706054\times10^{24}\ \mathrm{m}^{-2}$, agreeing with $-m^2c^2/\hbar^2$ to the digits shown.

## Problem 7: The helicity pieces and the piece determinant

**Statement.** Show that left multiplication by the helicity element commutes with the wave element, that the carrier splits into two two-dimensional pieces, one per helicity, compute the determinant of the pair on each, and read the mass shell as the vanishing of that determinant.

**Solution.** The free symbol is the element $i\tilde P$, and the massive equation is the pair of §*The Field and the Equation*.

**The scalar square.** The square of the wave element is not scalar, its product with its conjugate is: $\tilde K^{\natural}\tilde K=p^2$, by the collapse of Problem 3. The scalar datum of the wave is that product and not the square.

**The helicity grading.** For $\vec p\neq0$ put

$$
\tilde{Ζ}=i\,\vec u_p,\qquad \tilde{Ζ}^2=i^2\,\vec u_p^{\,2}=(-1)(-e_t)=e_t ,
$$

so that left multiplication by $\tilde{Ζ}$ has eigenvalues $\pm1$, each twice, and its two eigenspaces are two-dimensional. It commutes with the symbol: both are left multiplications by elements, and the two elements commute because $\vec u_p$ is proportional to $\vec k$. Left multiplications by commuting elements therefore commute, and the symbol keeps the two eigenspaces of $\tilde{Ζ}$. Each carries a two-dimensional piece of the carrier, one of each value.

**The piece determinant.** On a piece the pair, written on the two parts, has the two diagonal entries $-m$ and the two off-diagonal entries $i\tilde P$ and $i\tilde P^{\natural}$. The four are left multiplications by elements, and the elements commute, so the determinant of the pair is the determinant of the entries taken as numbers of that commutative algebra:

$$
\det=-m\cdot(-m)-(i\tilde P)(i\tilde P^{\natural})=m^2+\tilde P\tilde P^{\natural}=m^2-p^2 .
$$

The same number comes from the spectrum. The off-diagonal block squares to $(i\tilde P)(i\tilde P^{\natural})=p^2$ times the identity, so for $p^2>0$ the two eigenvalues of the block on the piece are

$$
-m+\sqrt{p^2},\qquad -m-\sqrt{p^2},
$$

and their product is $m^2-p^2$. The mass term is a multiple of the identity, so it shifts the two eigenvalues equally and enters the piece determinant once, and the determinant of the whole symbol is the product over the two pieces,

$$
\boxed{\;\det_{\mathrm{pair}}=\bigl(m^2-p^2\bigr)^2\;}
$$

the square of the Klein–Gordon symbol. The two pieces carry the same pair of eigenvalues: they are isospectral, and the common value of their determinants is the datum a single piece carries.

**The mass shell is the vanishing of a piece determinant.** Each determinant is $m^2-p^2$, so the pair is singular exactly when $p^2=m^2$. At that momentum each piece has a one-dimensional kernel: two zero modes, one per helicity, and these are the two helicity states of the particle. Off the shell each piece is invertible and the propagator is the inverse of the pair.

**Worked case, $\vec p\parallel\vec e_z$.** With $B=\lvert\vec p\rvert$ and the mass $m$, the pieces are the two helicity eigenspaces. For $m=1.3$, $E=2$, $B=0.9$: $p^2=3.19$ and $\sqrt{p^2}=1.786057$, so each piece determinant is $m^2-p^2=-1.5$, each piece spectrum is $\{-3.086057,\,0.486057\}$, and the determinant of the pair is $2.25=(m^2-p^2)^2$.

**Worked case, on the shell.** For $m=1.3$ and $\vec p=(0.4,-0.7,0.9)$ the energy is $E=\sqrt{m^2+\vec p^{\,2}}=1.774824$. Each piece determinant is zero, each piece spectrum is $\{-2m,\,0\}=\{-2.6,\,0\}$, and the pair has rank two, with a one-dimensional kernel per helicity.

**Numerical check.** The identities were recomputed on 100 random real four-momenta. The departure of the symbol from commuting with left multiplication by $\tilde{Ζ}$ was at most $5.4\times10^{-16}$; $\tilde K^{\natural}\tilde K$ and $\tilde P\tilde P^{\natural}$ departed from $\pm p^2$ by nothing to machine precision; $\tilde{Ζ}^2$ from $e_t$, $2.2\times10^{-16}$; the eigenvalues of the block from $-m\pm\sqrt{p^2}$, $8.0\times10^{-15}$; the product of the eight eigenvalues from $(m^2-p^2)^4$, $1.4\times10^{-57}$; and the amplitude ratio of Problem 1 from $(E\mp\lvert\vec p\rvert)/(E\pm\lvert\vec p\rvert)$ to $1.6\times10^{-14}$ relative. The two kernels of Problem 4 were recomputed on six null momenta: each of two complex dimensions, disjoint, and the helicity residual at most $6.5\times10^{-15}$.

**What the splitting is, and what it is not.** It says that the mass does not see the helicity, and therefore that a massive state is a pair of helicity pieces with equal spectra and unequal contents. The numbers inside a piece depend on the choice of basis within an eigenspace and are not physical; the determinant and the spectrum are. Three boundaries belong with the statement. At $\vec p=0$ the element $\tilde{Ζ}$ is undefined: the wave element is $im\,e_t$ and the pair is $-\tilde{Ξ}^{\mathrm{sp}}_R=m\tilde{Ξ}^{\mathrm{sp}}_L$, so the split is the split into the two values, the rest-frame split of Problem 1, and the label is a rest-frame value and not the helicity. For a spacelike momentum $p^2<0$ the two eigenvalues are complex and the piece determinant $m^2+\lvert p^2\rvert$ does not vanish: that is the off-shell region, not a second shell. For a null momentum $p^2=0$ the identity still holds, the piece determinant vanishes, and the kernel is two-dimensional and entirely of one helicity: this is the massless case of Problem 4.

## Summary

The seven problems test the parent's plane-wave solutions and confirm them in the algebra.

1. **The solutions.** Eliminating the second part gives the mass shell $E^2=\vec p^{\,2}+m^2$; on it the second part is free and the first is $\frac1m\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R$, the two parts standing in the norm ratio $(E\mp\lvert\vec p\rvert):(E\pm\lvert\vec p\rvert)$ for helicity $\pm1$. At rest $\tilde w_L(0)=-\tilde w_R(0)$, with basis $e_t-i\vec e_z$ and $\vec e_x+i\vec e_y$ for the part of value $R$; in the other reading the same elements are read on $\vec e_x$.
2. **Normalisation.** The covariant values $2m$, $-2m$ and $0$ follow from the single identity $(i\vec u_p)^2=e_t$ and from the geometric mean $\sqrt{E^2-\vec p^{\,2}}=m$; the Hermitian products are $2E$.
3. **Spin sums.** For every element, $\sum_\pm\tilde w_\pm\langle\tilde w_\pm,\tilde{Ξ}\rangle_{\mathrm D}=(i\tilde P+m)\tilde{Ξ}$ and $\sum_\pm\tilde v_\pm\langle\tilde v_\pm,\tilde{Ξ}\rangle_{\mathrm D}=(i\tilde P-m)\tilde{Ξ}$ read as products of elements; the closure $\tilde\nabla^{\natural}\tilde\nabla=\Box$ gives $\Box=m^2$ on the shell, and $\tilde P^{\natural}\tilde P=-m^2$.
4. **Massless limit.** The pair decouples, the field annihilated by $\tilde\nabla$ keeps one helicity and the field annihilated by $\tilde\nabla^{\natural}$ the other, and the two labels are locked: positive helicity with the first member and negative helicity with the second.
5. **The two parts.** The value is read by $\tilde Q\mapsto-i\tilde Q\vec e_z$, of spectrum $+1,+1,-1,-1$; a left multiplication keeps it and a right multiplication by $\vec e_x$ or $\vec e_y$ exchanges it; the change of the reading is right multiplication by $\tilde Q_{\mathrm{disp}}=(e_t+\vec e_y)/\sqrt2$, which sends the reading from $\vec e_z$ to $\vec e_x$ and touches no derivative.
6. **Mass shell.** The condition $\tilde P\tilde P^{\natural}=-m^2c^2$ is the quaternionic-norm statement $\langle\tilde P/\hbar\rangle_{\natural}=-m^2c^2/\hbar^2$, and reproduces $E^2=\vec p^{\,2}c^2+m^4c^4$.
7. **Helicity pieces.** The scalar square of the wave is $\tilde K^{\natural}\tilde K=p^2$; the symbol commutes with left multiplication by $\tilde{Ζ}=i\vec u_p$, so the carrier splits into two two-dimensional eigenspaces of piece determinant $m^2-p^2$; the pieces are isospectral, the determinant of the pair is $(m^2-p^2)^2$, and the mass shell is the vanishing of either piece determinant, with a one-dimensional kernel per helicity.

Two objects are needed by the exercise and are not given in the parent: the negative-frequency solutions $\tilde v$ (Problem 1) and the change-of-reading element $\tilde Q_{\mathrm{disp}}$ (Problem 5). The constructions above reproduce the parent's stated results.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\tilde\nabla$ | The biquaternionic gradient, $\sum_\mu e_\mu\,\partial/\partial Q_\mu$, four components |
| $\tilde\nabla^{\natural}$ | Its quaternion conjugate, $\sum_\mu\varepsilon_\mu e_\mu\,\partial/\partial Q_\mu$ |
| $\Box=\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla$ | The d'Alembertian, $\partial^2/\partial Q_t^2+\Delta_Q$ |
| $\tilde Q\mapsto-i\tilde Q\vec e_z$ | The action that reads the value; spectrum $+1,+1,-1,-1$ |
| $\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}}_L+\tilde{Ξ}^{\mathrm{sp}}_R$ | The Dirac field and its two parts, values $-1$ and $+1$ |
| $\tilde P=i k_0e_t+\vec k$ | Wave element of the plane wave, $k_0=E$, $\vec k=\vec p$ |
| $\tilde K=k_0-i\vec k=-i\tilde P$ | The same wave read by the gradient; $\tilde K^{\natural}\tilde K=p^2$ |
| $i\tilde P\,\tilde{Ξ}^{\mathrm{sp}}_R=m\tilde{Ξ}^{\mathrm{sp}}_L$ and $i\tilde P^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=m\tilde{Ξ}^{\mathrm{sp}}_R$ | The pair: the gradient and the mass, momentum space |
| $\langle\tilde{Ξ}^{\mathrm{sp}},\tilde{Ξ}\rangle_{\mathrm D}=\mathrm{Tr}\bigl(\tilde{Ξ}^{\mathrm{sp}*}\tilde{Ξ}\,i\vec e_x\bigr)$ | Dirac pairing, twisted by the timelike unit |
| $\tilde Q_{\mathrm{disp}}=(e_t+\vec e_y)/\sqrt2$ | Change of the reading, $\vec e_z$ to $\vec e_x$ |
| $\tilde P\tilde P^{\natural}=-m^2c^2$ | Mass-shell condition |
| $p^2=E^2-\vec p^{\,2}$ | Interval of the four-momentum, $\hbar=c=1$ |
| $m^2-p^2$ | Piece determinant, repeated on the two pieces |
| $\tilde{Ζ}=i\vec u_p$, $\vec u_p=\vec p/\lvert\vec p\rvert$ | Helicity element, $\tilde{Ζ}^2=e_t$; its two values grade the carrier |
| $-m\pm\sqrt{p^2}$ | Spectrum of the pair on a helicity piece |

## Further Reading

- The operator used above: [Operator and Calculus Conventions](operator-and-calculus-conventions.html), for the gradient, its conjugate, and the d'Alembertian.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the plane-wave solutions, the normalisations, and the spin sums in the standard notation.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the spin sums, the two representations, and the Lorentz generators.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the two representations, the normalisation, and the completeness relations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), as the record of the formulation the corpus replaced.
- The representation theory used above: [The Polarized Module of the Biquaternion Algebra](../articles_maths/the-polarized-module-of-the-biquaternion-algebra.html), for the two parts of an element and their dimensions.
- The parent article of this exercise: [The Biquaternion Dirac Equation — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html), and its companions [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) and [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html).
