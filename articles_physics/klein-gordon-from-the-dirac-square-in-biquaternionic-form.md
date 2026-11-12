# __Klein–Gordon from the Dirac Square in Biquaternionic Form__

## Introduction

The biquaternionic Dirac equation is first order. Its mass term is the central scalar $m$, and the equation is the pair

$$
\tilde\nabla_\Phi\tilde{Ξ}_{R} = k_m\tilde{Ξ}_{L}, \qquad (\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} = k_m\tilde{Ξ}_{R},
$$

in which each member sets the gradient of one chiral half equal to $m$ times the other. The companion article *The Dirac Equation in Biquaternionic Form* records, in a single paragraph, that applying $(\tilde\nabla_\Phi)^{\natural}$ to the first member and substituting the second gives $\Box\tilde{Ξ}_{R} = k_m^{2}\tilde{Ξ}_{R}$, so that each chiral component satisfies the Klein–Gordon equation. That paragraph is the hinge between the two halves of this category: it is where the relativistic quantum theory of spin $0$ and the relativistic quantum theory of spin $\tfrac12$ meet. This article reconstructs the passage in full, once in the algebra and once on the chiral pair, settles what the passage carries and what it drops, and then runs the passage the other way, where the second chiral half turns out to be the gradient of the first.

Two operators carry the name *Dirac operator* in this corpus, and they are the two faces of one square. The **one-sided** operator is the gradient $\tilde\nabla_\Phi$, which acts by multiplication on the algebra, and the equations it obeys are the chiral pair above. The second object is the same two gradients acting on an ordered pair of elements, and it is **two equations and not one operator**:

$$
\tilde\nabla_\Phi\tilde{Ξ}_{R}=k_m\tilde{Ξ}_{L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=k_m\tilde{Ξ}_{R},
\qquad
\tilde{Ξ} = (\tilde{Ξ}_{L},\tilde{Ξ}_{R}),
$$

one member per chiral half, the first acted on by $\tilde\nabla_\Phi$ and the second by $(\tilde\nabla_\Phi)^{\natural}$. The corpus once gathered the two into a single letter and called it the **pair operator**; that letter is retired, because it hides the adjoint, the metric and the signature that the two lines show, and nothing below needs it. The pair holds no element beyond the two gradients, and nothing in it multiplies on the right: the corpus's *two-sided* operator, the one that multiplies on the left and on the right at once, is a different object on a different carrier. Both readings reach the same central $\Box$ from the same product. In the algebra the square is the **product** $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$, not $\tilde\nabla_\Phi$ alone, and the **conjugate** cancels the cross terms; on the pair each half is acted on by one such product, so the composition is $\Box$ on both halves at once. Neither reading makes the plain square $\tilde\nabla^2$ scalar: the conjugate is what does the work, and it has to be written in one form or the other. The section *The Square on the Chiral Pair* carries the second reading.

The question is sharp because the companion article on the Klein–Gordon equation asked the mirror-image question and returned a negative result. *The Klein–Gordon Equation in Biquaternionic Form* shows that $\Box - k_m^{2}$ has **no first-order scalar square root inside the algebra** $\mathbb{B}$: the first-order terms of a product $((\tilde\nabla_\Phi)^{\natural}+ A)(\tilde\nabla_\Phi + B)$ can be cancelled only with $B = -A$ and $A$ anticommuting with all three units $\vec e_x,\vec e_y,\vec e_z$, and no such element exists. If the Klein–Gordon operator has no scalar square root, how does a first-order equation — the Dirac pair — imply it? The answer, worked out below, is that the square root is **not scalar**: it is the gradient acting on the two chiral halves, with the mass the same scalar in each and the gradients exchanging them. The scalar obstruction of the spin-$0$ article is exactly the evidence that the square root must be operator-valued. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

Three boundaries are respected. The Klein–Gordon **propagator** and the **scalar path integral** are the subject of the spin-$0$ companions and are not treated here. The d'Alembertian and its Green's functions are the subject of *The Biquaternion D'Alembertian and Its Green's Functions*, and the involution lattice is not reopened. What is treated here is the algebraic transfer from the first-order pair to the second-order equation, the kernel it produces, and the sense in which the transfer is irreversible.

Two conventions are load-bearing and are stated once. The d'Alembertian is the series convention,

$$
\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2 ,
$$

with $Q_t=i q'_t$, so that each time derivative carries the factor $(ic)^{-1} = -i/c$ when it is written in $r'_t$ and the time part is $-c^{-2}$ times the second derivative in $r'_t$. The imaginary unit satisfies $i^2 = -1$, and every product of two of them is reduced before a display is written: the collapse is what turns $(i\omega/c)^2$ into $-\omega^2/c^2$, and what makes $i\,\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_\Phi^{\natural})$ a purely imaginary exponent whose exponential has unit modulus. The mass parameter of the operator pair is measured in inverse-length units; restoring $\hbar$ and $c$, it is the inverse reduced Compton wavelength

$$
k_m=\dfrac{mc}{\hbar},
$$

so that the mass-shell condition reads $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural} = -m^{2}\,c^{2}$ and the second-order equation reads $(\Box - k_m^{2})\tilde{Ξ} = 0$. The two symbols stand in the ratio $k_m=mc/\hbar$, so a display that writes $m$ where an inverse length is meant is writing $k_m$; the second-order operator is $\Box-k_m^{2}$ in the algebra and carries the same $k_m^{2}$ with the physical units restored. This is the length the Klein–Gordon article carries as $1/k_m$, and the sign of $\Box$ is the series sign, the one *Exercise: Chirality and the Weyl Spinors* reaches from the squares of the two chiral equations.

## The Gradient and Its Square

Left multiplication by $\tilde\nabla_\Phi$ is the first-order operator, and $(\tilde\nabla_\Phi)^{\natural}$ is the quaternion conjugate of that same element, acting the same way, by multiplication on the left. The two products of the pair are the central scalar

$$
\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Box_\Phi .
$$

Neither equality is a square, and the distinction is the first thing the algebra contributes. Writing $\tilde\nabla = e_t\partial/\partial R_t + \vec\nabla$,

$$
\tilde\nabla^2 = \left(\partial^2/\partial R_t^2 - \lvert\vec\nabla\rvert^2\right)e_t + 2\,\partial/\partial R_t\,\vec\nabla ,
\qquad \lvert\vec\nabla\rvert^2 = \Delta ,
$$

so $\tilde\nabla^2 \neq \Box$. The spacelike cross terms do cancel, because the three vector units anticommute pairwise and $\vec\nabla\vec\nabla = -\lvert\vec\nabla\rvert^2e_t$ has no vector remainder; the cross term between the timelike direction and the vector part does not, because the timelike direction is carried by the unit $e_t$, which commutes with every $\vec e_\eta$ instead of anticommuting with it. The conjugate removes that remainder: $(\tilde\nabla_\Phi)^{\natural}$ enters with $-\vec\nabla$, the two mixed terms $-\partial/\partial R_t\,\vec\nabla$ and $+\vec\nabla\,\partial/\partial R_t$ cancel, and $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$ reduces to $(\partial^2/\partial R_t^2 + \lvert\vec\nabla\rvert^2)e_t$.

The conjugate is therefore what completes the square, and the two facts it uses are properties of the basis: $\vec e_x,\vec e_y,\vec e_z$ anticommute pairwise, and $e_t$ commutes with all three. Both are read from the multiplication table, and no second structure is needed. The root of $\Box$ inside the algebra is therefore the pair $(\tilde\nabla_\Phi,(\tilde\nabla_\Phi)^{\natural})$, never one gradient alone. No array and no frame enters the computation: a component check in a chosen basis must return the same element, because the basis is not part of the operator, and the reduction below stays with the operator.

## The Chiral Pair and the Two Reductions

The biquaternionic equation is not a single first-order equation in the algebra but the pair

$$
\tilde\nabla_\Phi\tilde{Ξ}_{R} = k_m\tilde{Ξ}_{L}, \qquad (\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} = k_m\tilde{Ξ}_{R},
$$

whose two members carry the two chiral halves. The reduction is a two-line computation. Apply $(\tilde\nabla_\Phi)^{\natural}$ to the first member:

$$
(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\tilde{Ξ}_{R} = (\tilde\nabla_\Phi)^{\natural}\!\left(k_m\tilde{Ξ}_{L}\right) = k_m(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} = k_m^{2}\tilde{Ξ}_{R},
$$

where the middle equality uses that $m$ is a scalar and the last uses the second member. Since $(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Box_\Phi$ is central,

$$
\boxed{\;\left(\Box-k_m^{2}\right)\tilde{Ξ}_{R} = 0\;}.
$$

Applying $\tilde\nabla_\Phi$ to the second member instead gives the same statement for $\tilde{Ξ}_{L}$:

$$
\boxed{\;\left(\Box-k_m^{2}\right)\tilde{Ξ}_{L} = 0\;}.
$$

Three features of this reduction deserve to be named, because they are what the algebra contributes and not merely what it transcribes.

First, the reduction uses the **two different gradients**. It is the passage from $\tilde\nabla_\Phi$ to $(\tilde\nabla_\Phi)^{\natural}$ that produces a central scalar, as the previous section showed: $\tilde\nabla_\Phi$ alone squares to a non-central element, and only the product $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$ is central. The square of the Dirac pair is the biquaternion norm $\langle\tilde\nabla_\Phi\rangle_{\natural} = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$, exactly as $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ is the biquaternion norm of an element — the observation the Klein–Gordon article makes about its own operator.

Second, the reduction eliminates **both** members of the pair at once. It is not that one chiral half obeys Klein–Gordon and the other does not; the mass couples them, so that squaring forces each half onto the same second-order shell. A mass that acted within each half alone would leave two separate first-order equations, each of which squares to a mass term beside a non-central $\tilde\nabla^2$; the coupling is what puts $\tilde\nabla_\Phi$ on one half and $(\tilde\nabla_\Phi)^{\natural}$ on the other, so that the second member converts the first-order left-hand side into the central $\Box$.

Third, the reduction is **linear in the mass squared**. The second-order equation knows only $m^2$. It has no memory of the sign of $m$ and no memory of the chirality that carried it. That loss is the subject of *What the Square Carries and What It Does Not*.

## The Square in the Biquaternion Algebra

The gradient and its conjugate are

$$
\tilde{\nabla} = e_t\partial/\partial R_t + \vec e_x\partial/\partial R_x + \vec e_y\partial/\partial R_y + \vec e_z\partial/\partial R_z,
$$

$$
\tilde{\nabla}^{\natural} = e_t\partial/\partial R_t - \vec e_x\partial/\partial R_x - \vec e_y\partial/\partial R_y - \vec e_z\partial/\partial R_z .
$$

Both operators act by multiplication, $\tilde\nabla_\Phi\tilde{Ξ}$ and $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}$, and two multiplications compose as the multiplication by the product: $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}$ is a single multiplication, by the element $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$, whose value on $\tilde{Ξ}$ is read off once that element is scalar — which it is, and that is what the next display shows.

Their product is central and scalar:

$$
\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= \Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2 = \Box_\Phi .
$$

The cancellation of the mixed terms uses the quaternion multiplication table twice: the spacelike ones cancel because $\{\vec e_j,\vec e_\eta\} = 0$ for $j\neq k$, the timelike ones because the scalar part commutes with the vector part. This is why $\Box$ is scalar and central, and why it acts on a biquaternion field coefficient by coefficient,

$$
\Box\tilde{Ξ} = \sum_{\nu\in\{t,x,y,z\}}(\BoxΞ_\nu)\,e_\nu ,
$$

with no mixing of components. The spin-$0$ article records this as the reason its equation decouples into four complex scalars; here the same centrality is what lets the square of the Dirac pair produce a single second-order equation rather than a system.

The mass is a **central scalar** too: $m$ commutes with $\Box$ and with the chirality of each half alike, and that is exactly why it passes through the gradient and lets the substitution above go through. Its coupling is not a property of $m$ but of the pair: the mass multiplies within a chiral half, the gradient maps one half into the other, and it is that mismatch that makes the pair two coupled equations rather than two separate ones. Squaring moves the mass across one gradient, and because $m$ is central the two orders agree. What the square then loses is the coupling — which half the mass connects — not its value, which survives as $m^2$. In the algebra the reduction is therefore

$$
(\tilde\nabla_\Phi)^{\natural}\!\left(\tilde\nabla_\Phi\tilde{Ξ}_{R}\right) = (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\tilde{Ξ}_{R} = \Box_\Phi\tilde{Ξ}_{R} ,
\qquad
k_m(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} = k_m^{2}\tilde{Ξ}_{R} ,
$$

and the equality of the two expressions is the equation $(\Box-k_m^{2})\tilde{Ξ}_{R} = 0$. Nothing in this step needs an array, a basis or a frame: it is the quaternion identity $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= \Box_\Phi$ applied to the pair.

### The Square in the Reduced Theory

The reduction to one spatial dimension isolates the mechanism without the bookkeeping of three. Take

$$
\tilde{\nabla} = e_t\partial/\partial R_t + \vec e_x\partial/\partial R_x, \qquad
\tilde{\nabla}^{\natural} = e_t\partial/\partial R_t - \vec e_x\partial/\partial R_x,
\qquad
\Box = \partial^2/\partial R_t^2 + \partial^2/\partial R_x^2 .
$$

The chiral pair retains its form and the reduction gives $(\Box-k_m^{2})\tilde{Ξ}_{L,R} = 0$ exactly as before. Each half is a whole biquaternion in the reduced theory as in the full one, so the chirality still splits the pair in two and the mass couples the halves exactly as before. The plane-wave substitution gives $\tilde P_{\Phi} = i\omega/c\,e_t + k\vec e_x$ and

$$
\tilde P_{\Phi}\tilde P_{\Phi}^{\natural} = -\omega^2/c^2 + k^2 = -k_m^{2},
\qquad\text{hence}\qquad
\omega^2 = k^2c^2 + k_m^{2}c^2 ,
$$

the 1+1-dimensional dispersion. Everything the three-dimensional case does, the reduced case does with a single wave number, and the second-order operator is again central.

The reduced form is the one in which the **factorisation** is most visible. Writing the pair as two coupled first-order equations and eliminating one half produces a single second-order equation for the other; conversely, the second-order equation is recovered from the pair but the pair is not recovered from it. This is the setting in which the supersymmetric interpretation of the first-order operator becomes transparent, because the pair is then a doublet of two elements, the mass the same scalar in each, and the two gradients the two maps that exchange them — the form *Supersymmetric Quantum Physics in the Biquaternion Framework* exploits.

## Why the Square Root Is Operator-Valued

The companion article on the Klein–Gordon equation proves an obstruction that appears, at first sight, to contradict the reduction just performed. Its theorem is that the scalar operator $\Box - k_m^{2}$ does not factor into first-order **scalar** operators inside $\mathbb{B}$. For constant biquaternion coefficients,

$$
((\tilde\nabla_\Phi)^{\natural}+ A)(\tilde\nabla_\Phi + B)
= \Box_\Phi + (A + B)\,\partial/\partial R_t + \sum_{\eta=x,y,z}\left(A\vec e_\eta - \vec e_\eta B\right)\partial/\partial R_\eta + AB,
$$

so cancelling the first-order terms requires $B = -A$ together with $A\vec e_\eta + \vec e_\eta A = 0$ for $\eta = x,y,z$. An element that anticommutes with all three quaternion units must vanish, and the reason is visible one unit at a time: the condition for $\vec e_\eta$ removes the scalar coefficient together with the coefficient of $\vec e_\eta$, so the three conditions hold together only on the zero element. With $A = 0$ the constant term is $AB = -A^2 = 0$, which cannot equal $-k_m^{2}$ for a finite mass, $k_m\neq0$, and no scalar factorisation exists.

The two results are consistent, and their consistency is the whole point. The Dirac square root is **not** a scalar factor of the form $\tilde\nabla_\Phi + A$ multiplying another scalar factor. It is an operator on the pair of chiral halves. On the pair the equation is two equations for two halves,

$$
\tilde\nabla_\Phi\tilde{Ξ}_{R}=k_m\tilde{Ξ}_{L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=k_m\tilde{Ξ}_{R},
$$

and its opposite-mass partner is the same two lines with $k_m$ written $-k_m$. *Operator and Calculus Conventions*, §*The Two First-Order Equations and Their Symbol*, writes the same pair and no letter for the two together. Because $m$ is central, the two lines compose cleanly, and composing each with the conjugate of the other gives

$$
\boxed{\;(\Box-k_m^{2})\tilde{Ξ}_{L}=0,\qquad(\Box-k_m^{2})\tilde{Ξ}_{R}=0\;},
$$

one equation per half, the two mass-gradient terms cancelling because the mass passes through the gradients.

Equivalently, the pair is the statement that each gradient carries one half into $k_m$ times the other, and composing a line with the conjugate of the other returns $k_m^{2}$ times that half, which is $(\Box-k_m^{2})\tilde{Ξ} = 0$ read on each half. This is the operator-valued square root: no scalar $\tilde\nabla_\Phi + A$ works, as the obstruction showed, but the pair of lines built from the conjugate pair does, because each line composed with its partner is the central $\Box$ on its half; the composition of the two mass-shifted maps is the central $\Box-k_m^{2}$ on each half. The obstruction identifies precisely the missing ingredient: a scalar square root would need an element anticommuting with all three vector units $\vec e_\eta$, $\eta=x,y,z$, and no biquaternion does; an operator-valued square root needs only that the **two different gradients cancel each other's vector parts**, which the conjugate pair does. The spin-$0$ no-go and the operator-valued square root are therefore one obstruction read two ways. This is what it means, in this framework, that the square root lives in the pair and not in the centre: the scalar field lives in $\mathbb{B}_{C}$, and the square root requires the exchange of two halves that only the pair carries.

## The Square on the Chiral Pair

The pair reading is written on the ordered pair of elements. Write $\tilde{Ξ} = (\tilde{Ξ}_{L},\tilde{Ξ}_{R})$ and write the two lines,

$$
\tilde\nabla_\Phi\tilde{Ξ}_{R}=k_m\tilde{Ξ}_{L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=k_m\tilde{Ξ}_{R},
$$

and compose each with the conjugate of the other,

$$
(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\tilde{Ξ}_{R}=\Box_\Phi\tilde{Ξ}_{R},
\qquad
\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=\Box_\Phi\tilde{Ξ}_{L},
$$

because each half is acted on by one product of the gradient with its conjugate, $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Box_\Phi$ being central. The pair is two lines and not a new object: it holds no element beyond the two gradients, and the mass acts on each half as the same scalar.

The pair is one member per chiral half:

$$
\tilde\nabla_\Phi\tilde{Ξ}_{R} = k_m\tilde{Ξ}_{L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} = k_m\tilde{Ξ}_{R} .
$$

**The chirality.** The two halves carry the signs $-1$ and $+1$, one sign per half; only the difference of the two signs carries content. The pair **exchanges** the halves, because each of its two lines carries one half into the other, and the mass **keeps** them, because it multiplies each half by the same scalar. That is the precise content of the phrase *a coupling between the halves*: no term carries $m$ from one half to the other; the gradient does the carrying, and the mass, the same in both halves, is what the carried field is set equal to. The two signs are the image on the pair of the central grading $i\tilde{Ζ}_{\mathrm{ad}}$ of the complexified algebra, outside $\mathbb{B}$ itself, which squares to the unit $e_t$; no element of $\mathbb{B}$ supplies it. The subscripts $L$ and $R$ are the letters the Dirac article gives the two chiral halves; here they label the two members of the pair, and nothing in this section computes them. Composing is what removes the exchange: the composition gives $\Box\tilde{Ξ}_{L}$ from the first line and $\Box\tilde{Ξ}_{R}$ from the second, and no half is carried into the other.

**The two statements, side by side.** The name now covers two statements, and they must not be read as one. The **first-order** statement is the pair

$$
\tilde\nabla_\Phi\tilde{Ξ}_{R} = k_m\tilde{Ξ}_{L}, \qquad (\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} = k_m\tilde{Ξ}_{R},
$$

with two gradients, one for each chiral half. The **second-order** statement is the composition

$$
(\Box-k_m^{2})\tilde{Ξ}_{L} = 0, \qquad (\Box-k_m^{2})\tilde{Ξ}_{R} = 0,
$$

one scalar operator on each half. The second is the square of the first: the two lines are the same two gradients, the exchange of halves is what turns one line into the other, and the mass, the same in both, is what the carried half is set equal to. The identity behind it is the one of the previous section, the composition of the two lines giving $\Box-k_m^{2}$ on each half, and both statements say that the mass enters the square squared.

## The Kernel and the Solution Space

Write the four-wavevector and the four-position as

$$
\tilde P_{\Phi} = i\frac{\omega}{c}e_t + \vec k_\Phi\in\mathbb{B}_{\Phi},
\qquad
\tilde R_\Phi = i r'_t\,e_t + \vec r\in\mathbb{B}_{\Phi},
$$

with $\vec k_\Phi = k_{\Phi x}\vec e_x + k_{\Phi y}\vec e_y + k_{\Phi z}\vec e_z$ and $\vec r = r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$. Here $\vec k_\Phi^2$ abbreviates the sum $k_1^2+k_2^2+k_3^2$ of the squares of the components, not the quaternion product, which is its negative, $\vec k_\Phi\,\vec k_\Phi = -\vec k_\Phi^2e_t$. The phase is $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_\Phi^{\natural}) = \vec k_\Phi\cdot\vec r - \omega r'_t/c$, the scalar part of the product with the conjugate four-position. The exponent $i\,\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_\Phi^{\natural})$ is a purely imaginary central element, so the exponential is central and differentiates as an ordinary exponential. On a plane wave,

$$
\partial/\partial r'_t \longmapsto -i\omega/c, \qquad \partial/\partial r_\eta\longmapsto ik_k, \qquad \partial/\partial R_t \longmapsto -\frac{\omega}{c},
$$

and therefore

$$
\tilde\nabla_\Phi \longmapsto -\frac{\omega}{c}e_t + i\vec k_\Phi, \qquad
(\tilde\nabla_\Phi)^{\natural}\longmapsto -\frac{\omega}{c}e_t - i\vec k_\Phi, \qquad
\Box_\Phi \longmapsto \frac{\omega^2}{c^2} - \vec k_\Phi^2 .
$$

The biquaternion norm of the wave biquaternion is

$$
\langle\tilde P_{\Phi}\rangle_{\natural} = \tilde P_{\Phi}\tilde P_{\Phi}^{\natural} = \left(i\frac{\omega}{c}\right)^2 + k_1^2+k_2^2+k_3^2 = -\frac{\omega^2}{c^2} + \vec k_\Phi^2 = -\Box ,
$$

the last equality holding on the plane wave, so the second-order equation $(\Box - k_m^{2})\tilde{Ξ} = 0$ is the mass-shell condition

$$
\tilde P_{\Phi}\tilde P_{\Phi}^{\natural} = -m^{2}\,c^{2},
\qquad\text{equivalently}\qquad
\omega^2 = \vec k_\Phi^2c^2 + k_m^{2}c^2,
$$

which is $E^2 = \vec p^2c^2 + m^2c^4$ under $E =\hbar\,\omega$, $\vec p =\hbar\,\vec k_\Phi$ and $k_m=mc/\hbar$. The sign is the series sign and is consistent with the Klein–Gordon article: the operator $\Box - k_m^{2}$ vanishes on the same shell on which the biquaternion norm equals $-k_m^{2}$.

The kernel of the square is larger than the kernel of the pair, and the difference is the information the square discards. For a fixed three-momentum $\vec p$, a **scalar** field obeying the Klein–Gordon equation has a two-dimensional complex solution space, spanned by the positive- and negative-frequency modes $\exp(\mp i(Er'_t/c-\vec p\cdot\vec r))$. A biquaternion field has four complex coefficients, and $(\Box - k_m^{2})$ acts coefficient by coefficient without mixing them, so the same pair of modes occurs once for each coefficient: an eight-dimensional complex solution space at fixed $\vec p$. The pair carries two such fields, so its second-order solution space at fixed $\vec p$ is sixteen-dimensional.

The first-order equation selects **half** of that space, and its solution is fixed by one half alone. Given $\tilde{Ξ}_{R}$, the first member defines $\tilde{Ξ}_{L} = m^{-1}\tilde\nabla_\Phi\tilde{Ξ}_{R}$, and the second member then holds exactly when $(\Box - k_m^{2})\tilde{Ξ}_{R} = 0$. On the mass shell at fixed $\vec p$, $\tilde{Ξ}_{R}$ is an arbitrary element of $\mathbb{B}$ at each frequency sign — four complex coefficients at $\exp(-i(Er'_t/c-\vec p\cdot\vec r))$ and four at $\exp(+i(Er'_t/c-\vec p\cdot\vec r))$ — so the pair's solution space is eight-dimensional, half of the sixteen. Each of the eight modes is annihilated by $\Box - k_m^{2}$, because that operator acts on each coefficient separately and the plane wave is its eigenfunction, but the converse fails: a general second-order solution of the pair is a combination of **sixteen** independent modes with arbitrary coefficients, and the two members cut that space down to eight by relating the halves at each frequency. The square therefore has a kernel twice as large as the pair's; it is a necessary condition, not a sufficient one.

The same count can be read off the algebra. The square is $\Box - k_m^{2}$ acting in each half separately, and it annihilates each half independently; the first-order pair is the same operator with the two gradients exchanged between the halves and set equal to $k_m\tilde{Ξ}$, which locks the two halves together. The square forgets the lock, and the lost information is exactly the relation that the lock imposes.

## The Massless Square and the Chiral Split

Setting $k_m = 0$, the massless limit, removes the coupling and separates the two halves:

$$
\tilde\nabla_\Phi\tilde{Ξ}_{R} = 0, \qquad (\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} = 0 .
$$

Each is a first-order equation whose conjugate product is the massless $\Box$, so each chirality separately obeys $\Box\tilde{Ξ} = 0$. The reduction, however, now carries no information: at $k_m = 0$ the pair is two independent first-order equations, and squaring either one loses the chirality that distinguished it from the other. This is the degenerate case of the general statement, and it is the biquaternion form of the standard fact that a massless Dirac field is two independent massless chiral fields, each of which satisfies the massless Klein–Gordon equation. The spin-$0$ operator of that article, $\Box - k_m^{2}$, reduces at $k_m = 0$ to exactly the conjugate product of the two gradients, $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi$.

The mass is therefore what makes the square **imply** the first-order equation rather than merely follow from it: at $k_m\neq0$ the two chiral equations are coupled by the mass, the square of the coupled system is the single scalar operator $\Box - k_m^{2}$, and the first-order pair is recovered from the square only together with the chirality lock. At $k_m = 0$ there is no lock and no recovery; the square is strictly weaker.

## What the Square Carries and What It Does Not

The transfer from the first-order pair to the second-order equation can now be accounted for.

**Carried.** The mass shell, with the relativistic dispersion $E^2 = \vec p^2c^2 + m^2c^4$; the mass-squared coefficient of the second-order operator, produced by the coupling rather than inserted; the decoupling of the four coefficient fields, a consequence of the centrality of $\Box$; the exchange of the two halves by the two lines, which is what makes each line carry one chiral half into the other in the first-order equation; and the statement that both chiral halves obey the same second-order equation, which is the pair identity, the composition of the two lines giving $\Box-k_m^{2}$ read on each half.

**Not carried.** The sign of the mass, the chirality of each half, the amplitude carried by each half, and the relation between the halves at each frequency branch. The square is even in $m$ and chirality-blind; it cannot distinguish a solution of the pair from a second-order solution that violates the pair. The passage is therefore one-way: every solution of the first-order pair is a solution of the second-order equation, and not conversely.

**Not claimed.** The square does not turn the spin-$\tfrac12$ field into a spin-$0$ field. The Klein–Gordon equation is obeyed by each **component**, but the object that obeys it is a pair of biquaternion fields: the reduction is a statement about the operator, not about what the field is. The genuine spin-$0$ field of the companion article lives in the centre $\mathbb{B}_{C}$, where the Klein–Gordon equation is the whole of the dynamics; the spin-$\tfrac12$ field lives in the pair, where the Klein–Gordon equation is the square's shadow and the first-order pair is the dynamics. The two share the operator and the mass shell, and nothing else. That is the precise sense in which this subcategory closes the loop to the spin-$0$ subcategory without absorbing it: the second-order equation is recovered, and what is recovered is exactly the part of the spin-$\tfrac12$ theory that the spin-$0$ theory already contained.

There is a final structural remark. The passage from the pair to the square is the passage from an operator that exchanges the halves to one that acts in each. In the two lines the gradient exchanges the halves and the mass acts in each; composing the two mass-shifted maps cancels the exchange and leaves $\Box-k_m^{2}$ in each half, so what has been traced out is exactly the exchange. The sign attached to each half is the one the supersymmetric structure of the first-order operator exploits, and *Supersymmetric Quantum Physics in the Biquaternion Framework* develops it. The Klein–Gordon equation is the bosonic shadow of the fermionic square root: it is what remains of a first-order operator once the exchange of the two halves is cancelled.

In the algebra the only identities used are $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Box_\Phi$, which is exact, and the mass-shell condition $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural} = -m^{2}\,c^{2}$, which is the definition of the on-shell four-momentum; no array enters. The pair reading uses the same identity twice, once for each half: the composition is $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$ on one half and $(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi$ on the other. No array enters that reading either.

## The Converse Direction

*The Kernel and the Solution Space* measured what the square loses. The mirror question is what the **split** loses, and its answer is stronger: the second chiral half is a derivative of the first, and not independent data. Read the first member of the pair as a definition,

$$
\tilde{Ξ}_{L} :=\frac{1}{k_m}\tilde\nabla_\Phi\tilde{Ξ}_{R} ,
$$

and substitute it into the second member. The left-hand side becomes $\frac{1}{k_m}(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\tilde{Ξ}_{R}$, which is $\frac{1}{k_m}\Box\tilde{Ξ}_{R}$ because the product of the conjugate pair is the central scalar, so the second member reads

$$
\Box\tilde{Ξ}_{R} = k_m^{2}\tilde{Ξ}_{R} .
$$

The substitution is therefore exact in both directions:

$$
\begin{aligned}
&(\Box_\Phi-k_m^{2})\tilde{Ξ}_{R} = 0 \
&\quad\Longleftrightarrow\quad
\tilde\nabla_\Phi\tilde{Ξ}_{R} = k_m\tilde{Ξ}_{L},\qquad  (\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} = k_m\tilde{Ξ}_{R},
\qquad \tilde{Ξ}_{L} =\frac{1}{k_m}\tilde\nabla_\Phi\tilde{Ξ}_{R} .
\end{aligned}
$$

Read left to right, a Klein–Gordon field generates a Dirac field. Read right to left, the first half of any Dirac field obeys Klein–Gordon. The map

$$
\tilde{Ξ}_{R} \longmapsto \left(\tilde{Ξ}_{R},\ \frac{1}{k_m}\tilde\nabla_\Phi\tilde{Ξ}_{R}\right)
$$

is $\mathbb{C}$-linear and injective and is onto the solution space of the pair, so the free Dirac solutions stand in bijection with the free Klein–Gordon solutions of **one chiral half**: the same data, described twice. The second member is not a second equation: it is what the definition of the second half turns into once the first half is on shell.

The device is older than this algebra. The second-order form of the Dirac equation in two halves, with the other chiral half restored by differentiation, is Feynman and Gell-Mann's rewriting of the Dirac equation for the theory of the Fermi interaction. The algebra's contribution is not the device but the form it takes here: the restoring operator is the algebra's own gradient, and the exactness in both directions follows from the single identity $(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Box_\Phi$.

Nothing in the display is a property of plane waves; the only identity used is $(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Box_\Phi$, which is central. The equivalence was checked on plane waves at both frequency signs, with residual at the floating-point floor, and **off** the mass shell the same substitution leaves exactly

$$\frac{1}{k_m}(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\tilde{Ξ}_{R} - k_m\tilde{Ξ}_{R} =\frac{1}{k_m}\left(\Box_\Phi-k_m^{2}\right)\tilde{Ξ}_{R} ,
$$

which is the second member's defect, so the mass shell is the exact condition and not an approximation.

This does not contradict the one-way statement of *What the Square Carries and What It Does Not*. That statement is about the pair, whose second-order space is twice its first-order space; the present one is about a single chiral half, of which the pair takes all. The counts agree: at fixed momentum the on-shell half has complex dimension eight, four coefficients at each of the two frequency signs; the pair's solution space has the same dimension eight; and the second-order space of the pair has dimension sixteen.

### The Gradient as a Field Strength

If the first half is called a potential and the second a field strength, the pair says that the field is the derivative of the potential. The gradient alone suggests the redundancy such a description usually carries: if $\tilde\nabla_\Phi\kappa = 0$, the potentials $\tilde{Ξ}_{R}$ and $\tilde{Ξ}_{R} + \kappa$ generate the same second half. The freedom does not survive the pair, and it is the mass shell that removes it. The condition $\tilde\nabla_\Phi\kappa = 0$ is the massless chiral equation, so $\kappa$ obeys $\Box\kappa = 0$ while the potential obeys $\Box\tilde{Ξ}_{R} = k_m^{2}\tilde{Ξ}_{R}$; the sum obeys neither, and the second member fails by exactly $m\kappa$. A potential off the mass shell generates no solution of the pair. In the two-term form there is therefore no redundancy to quotient out: the first half is physical data, and the pair fixes the whole field from it.

The four-scalar form of the same construction, in Kassandrov's treatment, does carry a genuine redundancy, and the difference is worth recording because it is where the phrase *the Dirac field is a gauge field* comes from. There the potential is a set of four Klein–Gordon scalars $\xi_{\mathrm{scl}}$ and the field is $\xi = D^*\xi_{\mathrm{scl}}$, for the source's first-order operator $D^*$, whose source identity is the source's own equation $DD^* = \Box-k_m^{2}$. The corpus's form of that operator is the pair of lines, which compose to $\Box-k_m^{2}$ in each half, as *The Square on the Chiral Pair* shows; the two differ in the carrier, four scalars there and two biquaternion halves here. Two potentials differing by $\kappa$ with $D^*\kappa = 0$ give the same field, and such a $\kappa$ is itself a Klein–Gordon solution, since $DD^*\kappa = 0$. The kernel of $D^*$ is the conjugate Dirac equation, which is the shape the electromagnetic case takes: there the potentials are defined up to the gradient $\tilde\nabla_\Phi\alpha$, the field is blind to it, and the gauge functions that survive the Lorenz condition are the ones with $\Box\alpha = 0$ — the same two-step structure, with the constraint on the gauge function carried by the field equation instead of by a subsidiary condition. The corpus keeps the two-term form, which is sharper, a doublet rather than a quadruple, and which has nothing to quotient out.

One step of the source's argument is not adopted. Kassandrov reads the construction as evidence that the transformation law of the field is not forced, taking the generating half to transform as a pair of scalars and the generated half then transforming nonlinearly. The corpus does not need that step and does not take it: the Lorentz action used here is the left action of the unit-norm biquaternions on the algebra, one action for every field, and a second realization on the coefficients is a different theory of the transformation law rather than a consequence of the pair.

### The Static Yukawa Pair

Take the generator to be the Yukawa potential, the static spherically symmetric solution of the massive Klein–Gordon equation:

$$
\tilde{Ξ}_{R} = \frac{e^{-k_m r}}{r},
\qquad
r = \lvert\vec r\rvert .
$$

It solves the equation because $\Delta\left(e^{-k_m r}/r\right) = k_m^{2}e^{-k_m r}/r$ away from the origin, which was checked symbolically. The definition gives the second half in closed form:

$$
\tilde{Ξ}_{L} =\frac{1}{k_m}\vec\nabla\frac{e^{-k_m r}}{r}
= -\frac{(1+k_m r)\,e^{-k_m r}}{k_m r^3}\,\vec r ,
\qquad
\vec r = r_x\,\vec e_x + r_y\,\vec e_y + r_z\,\vec e_z ,
$$

and the pair is exact: the first member holds by construction and the second, $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} = k_m\tilde{Ξ}_{R}$, was checked symbolically term by term. Three features belong to the algebra.

- The generator lies in the **scalar** part and the generated half in the **vector** part: scalar in, pure vector out. The static condition is what removes the timelike term of the gradient and leaves the vector part alone.
- The singularity **rises by one power**, from $1/r$ to $1/r^2$ times a radial vector, and the profile $(1+k_m r)e^{-k_m r}$ is what the derivative of the Yukawa tail produces.
- The pair is **spherically symmetric**: the scalar part is a function of $r$ alone and the vector part is a radial vector, so a rotation of the argument is undone by the rotation of the vector part. This is the corpus's form of the source's static spherically symmetric solution.

The two densities on this pair make the smallest illustration of the section, and the contrast is exact rather than approximate. The density of the pair is the sum of the Hermitian norms of its two halves, the extension to the pair of the identification the corpus's Dirac article makes between the Hermitian norm of a biquaternion field and the Dirac probability density:

$$
\rho^{(D)} = \langle\tilde{Ξ}_{R}\rangle_{*} + \langle\tilde{Ξ}_{L}\rangle_{*}
= \frac{e^{-2k_m r}}{r^2}\left(1 + \frac{(1+k_m r)^2}{k_m^{2}r^2}\right) > 0 ,
$$

positive everywhere, integrable at infinity, singular at the origin as $1/r^2$. Its companion is the Klein–Gordon density, and for this static configuration that one vanishes identically, because every term of it carries a time derivative. So the same pair carries a positive definite density and a density that is zero, and the pair of behaviours is what the corpus's forms separate: the Hermitian form $\langle\cdot\rangle_{*}$ is positive definite, while the quaternionic norm $\langle\cdot\rangle_{\natural}$ is the interval, indefinite and vanishing on the cone. The source writes the density as twice this one, its halves being pairs of complex components rather than biquaternions. From the pair it draws the further conclusion that the Dirac field escapes Pauli's theorem on the sign of the energy density; the corpus records the two densities and does not adjudicate the theorem.

### What the Correspondence Does Not Give

1. **No new solutions, and no privileged half.** The bijection repackages the free solution space. It also does not make the first half the more fundamental object, because the split is symmetric: parity sends $\tilde\nabla_\Phi$ to $(\tilde\nabla_\Phi)^{\natural}$ and back, so if $(\tilde{Ξ}_{R},\tilde{Ξ}_{L})$ solves the pair then so does $(\tilde{Ξ}_{L},\tilde{Ξ}_{R})$ composed with $\vec r\mapsto-\vec r$, which was checked on the symbol of the pair at both frequency signs. Kassandrov records the same exchange in external fields, where the halves trade places for anti-self-dual backgrounds.
2. **It fails under minimal coupling.** With $\tilde\nabla_\Phi\mapsto\tilde\nabla_\Phi - ie\tilde A_{\Phi}$ the two generalized gradients stop commuting, $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}\neq\tilde\nabla_{\mathrm{gco}}\tilde\nabla_{\mathrm{gco}}^{\natural}$, and what their commutator carries is the field strength; the product is then no longer the central scalar and the substitution no longer closes. A reduction survives only in a background whose complex field is (anti)self-dual, which is the boundary the hydrogen article meets in its own open questions.
3. **No physical content is added.** The distribution of the free modes over the mass shell, the amplitude of each half, the chirality of each half: all unchanged. What the section adds is the sentence that can be said about the pair once it is read as one equation and one definition — the second half is the gradient of the first.

The source builds infinite chains of solutions by feeding the generated half back as a new generator. In the algebra each step is one more application of the definition, and the corpus records the mechanism without reproducing the chains in the source's own arrangement of the components.

## Summary

The biquaternionic Dirac equation is the first-order pair $\tilde\nabla_\Phi\tilde{Ξ}_{R} = k_m\tilde{Ξ}_{L}$, $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} = k_m\tilde{Ξ}_{R}$. Applying $(\tilde\nabla_\Phi)^{\natural}$ to the first member and substituting the second gives $\Box\tilde{Ξ}_{R} = k_m^{2}\tilde{Ξ}_{R}$, and symmetrically for $\tilde{Ξ}_{L}$; both chiral halves obey the Klein–Gordon equation $(\Box-k_m^{2})\tilde{Ξ} = 0$ with the series d'Alembertian $\Box = \partial^2/\partial R_t^2 + \Delta$, which in physical units is $(\Box - k_m^{2})\tilde{Ξ} = 0$. The square is not the plain square: $\tilde\nabla^2 \neq \Box$, because the timelike unit $e_t$ commutes with the vector units and leaves the mixed term $2\,\partial/\partial R_t\,\vec\nabla$, and it is the conjugate product $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$ that cancels it. The conjugate is what completes the square, and the two facts it uses — the pairwise anticommutation of the three vector units and the commuting of $e_t$ — are read from the multiplication table.

On the pair the same square is written as two lines. The two lines exchange the two chiral halves and each composition gives $\Box$ in one half, because each half is acted on by one product of the gradient with its conjugate; the mass is the same scalar in both halves, so each line composed with the conjugate of the other is $\Box-k_m^{2}$ on its half. The two products are formed at once here, one per half, and the cancellation is the conjugate cancellation of the algebra; what the pair adds is the chirality that the square then loses.

The square root is not scalar. The companion article on the Klein–Gordon equation proves that $\Box - k_m^{2}$ has no first-order scalar factorisation in $\mathbb{B}$, because a scalar coefficient would have to anticommute with all three quaternion units and none does. The Dirac square root escapes the obstruction by being operator-valued and by exchanging the halves: it is the conjugate pair $(\tilde\nabla_\Phi,(\tilde\nabla_\Phi)^{\natural})$ acting on the two chiral halves, with the mass the same scalar in each. Written as the pair, the identity is that composing the two lines gives $\Box-k_m^{2}$ in each half; written as the two lines with the mass moved to the other side, it is that each line composed with its partner is $\Box$ in each half. The scalar no-go and the operator-valued square root are the same multiplication table seen from two sides.

The square carries the mass shell $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural} = -m^{2}\,c^{2}$, hence $E^2 = \vec p^2c^2 + m^2c^4$, and the mass-squared coefficient of the second-order operator; it does not carry the sign of the mass, the chirality of each half, or the relation between the halves that selects the first-order solution space from the larger second-order one. At fixed three-momentum the pair's second-order space has complex dimension sixteen and the first-order equation selects eight of them, so the square is a necessary and not a sufficient condition. The Klein–Gordon operator is the bosonic shadow of a first-order object that exchanges the two halves.

The converse holds exactly for the free pair. Read the first member as a definition, $\tilde{Ξ}_{L} =\frac{1}{k_m}\tilde\nabla_\Phi\tilde{Ξ}_{R}$; the second member then becomes $(\Box-k_m^{2})\tilde{Ξ}_{R} = 0$, so the free Dirac solutions stand in bijection with the free Klein–Gordon solutions of one chiral half, and the second half is the gradient of the first. In this two-term form there is no gauge freedom, because the only shift the gradient annihilates is the massless Weyl field, which takes the potential off the mass shell; the source's four-scalar form of the same construction does carry the residual gauge $\xi_{\mathrm{scl}}\mapsto\xi_{\mathrm{scl}}+\kappa$ with $D^*\kappa = 0$, and that is what earns the phrase *the Dirac field is a gauge field*. The correspondence is exact for the free field and stops at minimal coupling, where the commutator of the two generalized gradients is the field strength. Its smallest illustration is the static Yukawa pair, generator $e^{-k_m r}/r$ and second half $-(1+k_m r)e^{-k_m r}\vec r/(k_m r^3)$, on which the Dirac density is positive definite and the Klein–Gordon density vanishes.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\eta^2 = -e_t$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | Anti-Hermitian (material) and Hermitian (informational) sectors |
| $\tilde\nabla_\Phi\tilde{Ξ}_{R}=k_m\tilde{Ξ}_{L}$, $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=k_m\tilde{Ξ}_{R}$ | The pair, as two first-order equations; the two lines exchange the chiral halves, and each composed with its partner is $\Box$ in one half |
| $i\tilde{Ζ}_{\mathrm{ad}}$ | Central grading of the complexified algebra, outside $\mathbb{B}$; the signs $-1$ and $+1$ of the pair are its image |
| $\tilde{\nabla} = e_t\partial/\partial R_t + \sum_{\eta=x,y,z}\vec e_\eta\,\partial/\partial R_\eta$ | Biquaternionic gradient, the one-sided Dirac operator, acting by multiplication on the left |
| $(\tilde\nabla_\Phi)^{\natural}$ | Quaternion conjugate gradient |
| $\vec\nabla = \sum_{\eta=x,y,z}\vec e_\eta\,\partial/\partial R_\eta$ | Vector part of the gradient, $\lvert\vec\nabla\rvert^2 = \Delta$ |
| $\tilde{\nabla}^2 = \left(\partial^2/\partial R_t^2 - \lvert\vec\nabla\rvert^2\right)e_t + 2\,\partial/\partial R_t\,\vec\nabla$ | Square of the gradient alone; non-central, with a vector remainder |
| $\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2$ | d'Alembertian, series convention |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Biquaternion norm |
| $\tilde P_{\Phi} =\hbar\,(i\omega/c\,e_t + \vec k_\Phi)$ | Four-wavevector, $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural} = -m^{2}\,c^{2}$ |
| $\tilde R_\Phi = i r'_t\,e_t + \vec r$, with $\vec r = r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Four-position, phase $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_\Phi^{\natural}) = \vec k_\Phi\cdot\vec r - \omega r'_t/c$ |
| $1/k_m$ | The mass length of the operator pair, $\hbar/(mc)$ (inverse reduced Compton wavelength) |
| $\tilde\nabla_\Phi\tilde{Ξ}_{R} = k_m\tilde{Ξ}_{L}$, $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} = k_m\tilde{Ξ}_{R}$ | The one-sided pair; linear, with the mass the same scalar in each half |
| $\tilde{Ξ}_{L} =\frac{1}{k_m}\tilde\nabla_\Phi\tilde{Ξ}_{R}$ | The second half as the gradient of the first; the pair's equivalent form, exact whenever $(\Box-k_m^{2})\tilde{Ξ}_{R} = 0$ |
| $\langle\tilde{Ξ}\rangle_{*} = \sum_\mu\lvert\tilde{Ξ}_{\mu}\rvert^2$ | Hermitian norm of a field, positive definite; the Dirac density of the pair |
| $\tilde{Ξ} = (\tilde{Ξ}_{L},\tilde{Ξ}_{R})$ | The chiral pair as an ordered pair of elements |
| $E^2 = \vec p^2c^2 + m^2c^4$ | Dispersion relation |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original first-order equation and its second-order consequence.
- O. Klein, "Elektrodynamik und Wellenmechanik vom Standpunkt des Korrespondenzprinzips," *Zeitschrift für Physik* **41** (1927) 407–442, and W. Gordon, "Der Comptoneffekt nach der Schrödingerschen Theorie," *Zeitschrift für Physik* **40** (1926) 117–133, for the second-order relativistic wave equation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the first-order equation, its second-order square and the plane-wave solutions.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the square of the Dirac operator and the Weyl decomposition.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the five basis operators of the older frame and their representations, and the mass shell.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the even subalgebra and the square root of the wave operator.
- D. Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), and C. Doran and A. Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra interpretation of the Dirac operator and its square.
- S. S. Schweber, *An Introduction to Relativistic Quantum Field Theory* (Harper and Row, 1961), and A. I. Akhiezer and V. B. Berestetskii, *Quantum Electrodynamics* (Wiley, 1965), for the older arrangement of the Dirac equation in two halves and the squared equation in an external field.
- V. V. Kassandrov, "Gauge origin of the Dirac field and singular solutions to the Dirac equation," arXiv:1706.08397 (2017), for the Klein–Gordon potentials of the free Dirac field, the reduction of the quadruple to a doublet, the residual gauge of the four-scalar form, and the singular chains generated by differentiation; the earlier presentation of the same construction is arXiv:0907.4736 (2009), where the differentiation chain $\xi_N = D^*P_N\cdots D^*P_1\xi$ with $P_i\in SL(4,\mathbb{C})$ is generated by constant operators rather than by the potential gauge, and where the massive singular seed $Ξ = \mu\,e^{-imt}/r$ with $\mu = (x+iy)/(r+z)$ and its first Dirac descendant are displayed — a construction that stays on the potentials and has no image on the Dirac field itself, since $D^*P\kappa\neq0$ when $D^*\kappa = 0$. Its treatment of complexified external fields — the self-duality condition $\vec H = \pm i\vec E$, the reduction of the squared equation to the Klein–Gordon equation in the joint field of an electric charge and an imaginary magnetic monopole, the exchange of the two halves for anti-self-dual backgrounds, and the Coulomb ansatz $A_{\theta_{\mathrm{azm}}} = iΞ\tan(\theta/2)$ — is what open question 8 of the hydrogen article rests on.
- R. P. Feynman and M. Gell-Mann, "Theory of the Fermi interaction," *Physical Review* **109** (1958) 193–198, for the second-order form of the Dirac equation in two halves, with the other chiral half restored by differentiation, the device §*The Converse Direction* carries into the algebra.
- R. P. Feynman, "Space-time approach to non-relativistic quantum mechanics," *Reviews of Modern Physics* **20** (1948) 367–387, for the second-order wave equation as the square of a first-order operator in the path-integral setting.
