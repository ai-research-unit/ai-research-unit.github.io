# __The Dirac Oscillator in Biquaternionic Form__

## Introduction

The Dirac oscillator is the relativistic quantum system obtained from the free Dirac Hamiltonian by the non-minimal substitution

$$
\boxed{\;\vec p \;\longrightarrow\; \vec p - i m\omega \beta\vec r\;},
$$

introduced by Marcos Moshinsky and Adam Szczepaniak in 1989. Here $\vec p$ is the momentum operator, $p_\eta=-i\,\hbar\partial/\partial R_\eta$, and the source's equation is the Hamiltonian one,

$$
H = c\sum_\eta\alpha_\eta\left(p_\eta - i m\omega\beta Q_\eta\right) + \beta mc^2 ,
\qquad
H\tilde{Ξ}_{\mathrm{sp}} =i\,\hbar\frac{\partial}{\partial  h_t}\tilde{Ξ}_{\mathrm{sp}} .
$$

The substitution is "non-minimal" in the precise sense that it cannot be obtained from a gauge potential: it adds, to the odd (frame-anticommuting) part of the operator, a term linear in the position. The resulting system is exactly solvable, its non-relativistic limit is the three-dimensional isotropic harmonic oscillator together with a spin–orbit coupling of the same order as the level spacing, and it has become the standard laboratory for the relativistic treatment of confining interactions.

It belongs in this subcategory as the **exactly solvable external-potential problem** of the biquaternionic Dirac theory. The hydrogen atom, treated in the companion article *The Hydrogen Atom in Biquaternionic Form — The Relativistic Case*, is exactly solvable by a different mechanism (a Coulomb central field and a second-order radial reduction); the oscillator is exactly solvable because the two first-order operators of its pair can be multiplied in closed form, and the product is again a second-order operator, central apart from a single spin–orbit term. That is the same product as in *Klein–Gordon from the Dirac Square in Biquaternionic Form*, now with the position-dependent addition that makes the product a harmonic oscillator. A product available in closed form, plus a confining addition that is linear in the position, make the model the place where one sees concretely how the biquaternionic first-order operator behaves under multiplication by its conjugate.

The article derives the substitution, the split of a state into its two frame parts and the coupled pair those parts satisfy, the exact operator identity on multiplying the two first-order operators, and the spectrum; it then works the one-dimensional case for which everything is transparent, takes the non-relativistic limit, reads the result in the algebra, and connects the zero modes to the supersymmetric structure developed in the companion article *Supersymmetric Quantum Physics in the Biquaternion Framework*. Nothing below is written with a matrix, a column or a decomposition of the algebra: a state is an element, an operator is an action on it or the gradient, and no array appears.

**The gradient and the d'Alembertian.** Every derivative in this article is the corpus gradient. The conventions are stated once, here, and used without restatement:

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\,\frac{\partial}{\partial R_\mu},
\qquad
\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\,\frac{\partial}{\partial R_\mu},
\qquad
\Box=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\frac{\partial^2}{\partial R_t^2}+\Delta_Q ,
$$

with $\varepsilon=(1,-1,-1,-1)$ and $\Delta_Q=\sum_\eta\partial^2/\partial R_\eta^2$. Write $\vec\nabla=\sum_\eta\vec e_\eta\,\partial/\partial R_\eta$ for the spatial part, so that $\tilde\nabla=e_t\,\partial/\partial R_t+\vec\nabla$ and $\vec\nabla\vec\nabla=-\Delta_Q$. On the material sector $\mathbb{B}_{\Phi}$, where $Q_t=i q'_t$ and $\partial/\partial R_t=-i\,\partial/\partial r'_t$, the d'Alembertian is $\Box=\Delta-\partial^2/\partial {r'_t}^2$.

**Why the mass needs two fields.** The plain square of the gradient is not scalar. The three spatial units anticommute, so $\vec\nabla\vec\nabla=-\Delta_Q$ is scalar, but the time unit $e_t$ commutes with them instead of anticommuting, and the mixed term survives:

$$
\tilde\nabla^2=\frac{\partial^2}{\partial R_t^2}-\Delta_Q+2e_t\,\frac{\partial}{\partial R_t}\,\vec\nabla
\;\neq\;\Box .
$$

The quaternion conjugate removes that term, because $(\tilde\nabla_\Phi)^{\natural}$ enters with $-\vec\nabla$ and the two mixed terms cancel. The root of $\Box$ inside the algebra is therefore the **pair** $(\tilde\nabla_\Phi,(\tilde\nabla_\Phi)^{\natural})$, never one gradient alone. Consequently the free equation stays first order in one field, $\tilde\nabla_\Phi\tilde F=0$, and the massive equation needs two fields, the **chiral pair**

$$
\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R},
\qquad
k_m=\dfrac{mc}{\hbar},
$$

in which each member sets the gradient of one chiral half equal to $k_m$ times the other. No single field carries a mass in this algebra, and no display below writes one.

**The pair stays two lines.** The two lines are printed once each and never compressed into one operator on $\mathbb{B}\oplus\mathbb{B}$,

$$
\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R},
\qquad
\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi=\Box,
$$

one gradient per line and one slot per line. Nothing acts on the right: each line is built from one gradient and nothing else enters.

**The subscript.** The chirality is a value of the element: the test returns $L$ or $R$, and those are the two values. The letters are the Dirac ones, $L$ and $R$, the names of the two components, in the sense the corpus already uses for $\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{Ξ}_{\mathrm{sp},R}$. Every element is a sum of one of each, only the zero element is both, a product takes the letter of its right factor, and left multiplication keeps the letter. The subscript belongs to the element, not to a column: a unit, a product and a general element carry it, and a state carries it because a state is an element.

**The two gradings.** Chirality and the frame are different functions of the same state, and the oscillator separates the two. Chirality is the value of the previous paragraph. The frame is the action $\beta$ below, which is $+1$ on one part of a state and $-1$ on the other; the mass is diagonal in the frame and off-diagonal in the chirality, and the two labels are not interchangeable. The chiral pair above is the corpus equation for a free mass. The oscillator's substitution is built from $\beta$, so the oscillator is posed in the frame grading, and its pair is the same two-field structure with the mass in the diagonal slot and the derivative in the off-diagonal one. That is the only reason the pair below looks unlike the chiral pair, and it changes no physics: a two-field equation with the mass in one slot and the gradient in the other is the corpus's form of a massive first-order equation.

**Conventions.** The conventions are those of the companion articles — *Algebra and Element Conventions*, *Operator Family Conventions*, *Operator and Calculus Conventions*, *Frame and Metric Conventions* — and none is redefined. Two actions are the article's own, written out once,

$$
\beta:\ Q\longmapsto iQ\vec e_x,\qquad
\alpha_\eta:\ Q\longmapsto \vec e_\eta Q\vec e_z .
$$

The first is a **single right action**, the right multiplication by the element $i\vec e_x$; the second is a **two-sided action**, with the element $\vec e_\eta$ on the left and the element $\vec e_z$ on the right. Both are Hermitian and square to the identity, the mixed products are $\beta\alpha_\eta:Q\mapsto i\vec e_\eta Q\vec e_y$ and $\alpha_\eta\beta:Q\mapsto-i\vec e_\eta Q\vec e_y$, and $\beta\alpha_\eta\beta=-\alpha_\eta$. The non-minimal shift of the gradient is written once,

$$
\vec\nabla_\pm:=\vec\nabla\pm\dfrac{\omega\,k_m}{c}\,\vec r,
\qquad
\vec r=\sum_\eta\vec e_\eta Q_\eta ,
$$

so that $\vec\nabla_-\vec\nabla_+$ and $\vec\nabla_+\vec\nabla_-$ are the two orders of the shifted spatial gradient. That is all the body needs.

## The Non-Minimal Substitution

Minimal coupling replaces $\vec p$ by $\vec p - q\vec A$; the added term is a vector potential and enters the Hamiltonian through $\sum_\eta\alpha_\eta A_\eta$. The oscillator substitution is different in three ways, and each matters.

**It multiplies the position by $\beta$.** The added term is $-im\omega\beta\vec r$, not $-im\omega\vec r$. Because $\beta$ anticommutes with every $\alpha_\eta$, the product $\beta\alpha_\eta$, which is the two-sided action $Q\mapsto i\vec e_\eta Q\vec e_y$ contracted with the position, is frame-**odd**: it lies in the same grading class as the kinetic term built on $\vec p$, and in the opposite class from the mass $\beta mc^2$. In the algebra this is the statement that the substitution shifts the odd part of the operator while leaving the even part alone, which is why the product of the two first-order operators is again second order and central except for the spin–orbit term.

**The coefficient is imaginary, and the term is Hermitian.** A gauge interaction adds the real, Hermitian $q\vec A$ to $\vec p$; here the coefficient is $i$. In the actions the imaginary coefficient is spent on the action at once, because $\alpha_\eta\beta$ is the two-sided action $Q\mapsto-i\vec e_\eta Q\vec e_y$ and the two factors of $i$ multiply to $-1$:

$$
c\sum_\eta\alpha_\eta\left(-im\omega\beta Q_\eta\right)\tilde{Ξ}_{\mathrm{sp}}
=-icm\omega\sum_\eta\alpha_\eta\beta\,Q_\eta\,\tilde{Ξ}_{\mathrm{sp}}
=-cm\omega\sum_\eta \vec e_\eta\,(Q_\eta\tilde{Ξ}_{\mathrm{sp}})\,\vec e_y .
$$

The coefficient is now real, and the action $Q\mapsto\vec e_\eta Q\vec e_y$ is Hermitian: the adjoint of $Q\mapsto aQb$ is $Q\mapsto a^{*}Qb^{*}$, and the units satisfy $\vec e_\eta^{*}=-\vec e_\eta$ and $\vec e_y^{*}=-\vec e_y$, so the two sign changes cancel. The added term is therefore Hermitian, and so is $H$. What the imaginary coefficient signals is not a complex deformation — the spectrum below is real — but a term that is frame-odd, linear in the position and biquaternion-valued, which a gauge potential cannot produce.

**It is linear in the position**, so it grows without bound. The oscillator potential is confining, the spectrum is discrete, and the model is a relativistic confinement model rather than a scattering problem. This is the physical reason for its use in quark-confinement phenomenology, and the reason the spectrum consists of bound levels with the mass gap at their base.

**The shift of the gradient.** The substitution is a shift of the spatial part of the gradient and of nothing else, because the momentum operator is the spatial gradient: $p_\eta=-i\,\hbar\partial/\partial R_\eta$ gives

$$
\vec p - im\omega\beta\vec r \;=\; -i\,\hbar\left(\vec\nabla+\dfrac{\omega\,k_m}{c}\,\beta\vec r\right).
$$

The shift carries $\beta$, and $\beta$ is a right action, so the multiplied position acts first and the element $i\vec e_x$ acts last: the shift is $\dfrac{\omega\,k_m}{c}$ times the action $\tilde{Ξ}_{\mathrm{sp}}\mapsto(\vec r\tilde{Ξ}_{\mathrm{sp}})\,i\vec e_x$. On a state that $\beta$ fixes, that is the shift $\vec\nabla\to\vec\nabla_+$; on a state that $\beta$ negates, it is the shift $\vec\nabla\to\vec\nabla_-$. The two signs of one shift are the whole content of the substitution, and they are why the pair below has two lines.

**The pair.** The source's equation acts on one field and carries the mass in the diagonal slot. In the algebra that equation is not one equation but two, because the operator that multiplies the mass, $\beta$, is diagonal in the frame grading while every $\alpha_\eta$ is off-diagonal in it. Projecting the source's equation on the two frame parts, and using that $\alpha_\eta$ carries each part into the other, gives the coupled pair

$$
(E-mc^2)\tilde{Ξ}_{\mathrm{sp},+} =i\,\hbar\,c\bigl(\vec\nabla_+\tilde{Ξ}_{\mathrm{sp},-}\bigr)\omega ,
\qquad
(E+mc^2)\tilde{Ξ}_{\mathrm{sp},-} =i\,\hbar\,c\bigl(\vec\nabla_-\tilde{Ξ}_{\mathrm{sp},+}\bigr)\omega ,
\qquad
\omega=-\vec e_z ,
$$

where $\omega$ is the pseudoscalar of the algebra, $\omega^2=-e_t$, an element and not the central unit $i$; the oscillator frequency that multiplies $m$ is a real scalar and shares the letter, and it stands only where $m$ or $\hbar$ stands beside it. The right factor is the one the source's velocity action carries: the two-sided action $\alpha_\eta$ is the gradient's $\eta$-th term with $\vec e_z$ on the right, and $\vec e_z=-\omega$. The sign of the shift is the sign of $-\beta$ on the state the line acts on: the line for $\tilde{Ξ}_{\mathrm{sp},+}$ acts on $\tilde{Ξ}_{\mathrm{sp},-}$, where $\beta=-1$, so it carries $\vec\nabla_+$, and the line for $\tilde{Ξ}_{\mathrm{sp},-}$ acts on $\tilde{Ξ}_{\mathrm{sp},+}$, where $\beta=+1$, so it carries $\vec\nabla_-$.

Each right-hand side is the shifted gradient followed by one fixed right factor, the element $\omega$; the position enters the shift, and nothing else in it depends on the position. That is the shape the biquaternion reading below uses.

## The Frame Split and the Coupled Pair

A state is an element $\tilde{Ξ}_{\mathrm{sp}}$ of $\mathbb{B}$. The frame action $\beta$ takes the two values $+1$ and $-1$, so every state splits in exactly one way,

$$
\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},+} + \tilde{Ξ}_{\mathrm{sp},-},
\qquad
\tilde{Ξ}_{\mathrm{sp},+}=\tfrac12\bigl(\tilde{Ξ}_{\mathrm{sp}}+i\tilde{Ξ}_{\mathrm{sp}}\vec e_x\bigr),
\qquad
\tilde{Ξ}_{\mathrm{sp},-}=\tfrac12\bigl(\tilde{Ξ}_{\mathrm{sp}}-i\tilde{Ξ}_{\mathrm{sp}}\vec e_x\bigr),
\qquad
\beta\tilde{Ξ}_{\mathrm{sp},+}=\tilde{Ξ}_{\mathrm{sp},+},\quad \beta\tilde{Ξ}_{\mathrm{sp},-}=-\tilde{Ξ}_{\mathrm{sp},-} .
$$

The split is read on the element and not chosen in a basis: $\tilde{Ξ}_{\mathrm{sp},+}$ is the part with $\beta=+1$ and $\tilde{Ξ}_{\mathrm{sp},-}$ the part with $\beta=-1$. Since $\beta$ anticommutes with every $\alpha_\eta$, each velocity action carries $\tilde{Ξ}_{\mathrm{sp},+}$ into the part with $\beta=-1$ and $\tilde{Ξ}_{\mathrm{sp},-}$ into the part with $\beta=+1$; that is why the pair is coupled, and why no first-order equation survives for one part alone when $m\ne0$. The mass is diagonal in the same split, with the value $+mc^2$ on $\tilde{Ξ}_{\mathrm{sp},+}$ and $-mc^2$ on $\tilde{Ξ}_{\mathrm{sp},-}$.

The pair written above is the shape in which the oscillator is normally solved: the two frame parts are coupled by the two shifted gradients and the two conjugate signs of the substitution, and the coupling has the shape of a minimal coupling, with $\pm im\omega\vec r$ standing where the vector potential stands. Eliminating $\tilde{Ξ}_{\mathrm{sp},-}$,

$$
\tilde{Ξ}_{\mathrm{sp},-} =\frac{i\,\hbar\,c}{E+mc^2}\,\bigl(\vec\nabla_-\tilde{Ξ}_{\mathrm{sp},+}\bigr)\omega ,
$$

and substituting into the first line gives the second-order equation for the large part alone:

$$
\left(E^2 - m^2c^4\right)\tilde{Ξ}_{\mathrm{sp},+}
= c^2\mathcal{Q}_+\mathcal{Q}_-\,\tilde{Ξ}_{\mathrm{sp},+} ,
\qquad
\mathcal{Q}_\pm:\ i\,\hbar\,\tilde{Ξ}_{\mathrm{sp}}\,\longmapsto\bigl(\vec\nabla_\mp\tilde{Ξ}_{\mathrm{sp}}\bigr)\omega .
$$

The two first-order actions are adjoints of one another up to sign, $\mathcal{Q}_+^{\dagger}=-\mathcal{Q}_-$: the adjoint of the shifted gradient $\vec\nabla_-$ is $-\vec\nabla_+$, and $\omega=-\vec e_z$ is anti-Hermitian while the factor $i\,\hbar$ is Hermitian, so the two signs cancel. Both actions are built from the one gradient, and their product is what the next section evaluates. Everything now rests on that product.

## The Square of the Coupled Operator

The product is computed from two facts and from no matrix identity: the multiplication table of the three spatial units, and $[Q_\eta,p_\eta]=i\,\hbar$. The two facts do all the work, and they are the only places where the units and where $\hbar$ enter.

**The product is the shifted gradient twice.** The two first-order actions are $\hbar$ times the shifted spatial gradient, right-multiplied by $\omega$, and $\omega^2=-e_t$. The two right factors therefore collapse to $-e_t$, the overall sign flips, and

$$
\mathcal{Q}_+\mathcal{Q}_-=\hbar^{2}\,\vec \nabla_{-}\,\vec \nabla_{+},
$$

a left multiplication by the element-valued differential operator $\hbar^{2}\,\vec \nabla_{-}\,\vec \nabla_{+}$. That is the object the whole section evaluates. Its diagonal part is scalar; its off-diagonal part is not, and that is the whole story of the spectrum.

**The diagonal part.** The terms with equal indices are scalar operators, and their sum is

$$
\sum_\eta\bigl(p_\eta+im\omega Q_\eta\bigr)\bigl(p_\eta-im\omega Q_\eta\bigr)
= \vec p^{\,2} + m^2\omega^2\vec r^{\,2} + im\omega\sum_\eta\bigl[Q_\eta,p_\eta\bigr]
= \vec p^{\,2} + m^2\omega^2\vec r^{\,2} -3\,\hbar\,m\,\omega ,
$$

because $[Q_\eta,p_\eta]=i\,\hbar$ in each of the three spatial directions, the sum of the three gives $3\,i\,\hbar$, and $im\omega\,(3\,i\,\hbar)=-3\,\hbar\,m\,\omega$ through one more use of $i^2=-1$. In the algebra the same three terms are the diagonal of $\vec\nabla_-\vec\nabla_+$: the two shifts multiply to $-\frac{\omega^2\,k_m^{2}}{c^2}\vec r^{\,2}$, the two derivatives to $-\Delta_Q=\frac{\vec p^{2}}{\hbar^{2}}$, and the cross term of $\partial/\partial R_\eta$ with $Q_\eta$ in each direction gives the commutator, which is where the zero point comes from.

**The cross part.** A term with $j\ne k$ carries the product of two different spatial units, and that product is a unit again, $\vec e_j\vec e_\eta=\epsilon_{j\eta l}\vec e_l$ with $\epsilon_{xyz}=+1$. The pair of ordered terms with the indices exchanged carries the same unit with the opposite sign, so only the antisymmetric part of the coefficient survives, and it is

$$
\bigl(p_j+im\omega Q_j\bigr)\bigl(p_\eta-im\omega Q_\eta\bigr)-\bigl(p_\eta+im\omega Q_\eta\bigr)\bigl(p_j-im\omega Q_j\bigr)
= 2im\omega\bigl(Q_jp_\eta-Q_kp_j\bigr) = 2im\omega\sum_l\epsilon_{j\eta l}L_{\mathrm{orb},l}
$$

with $L_{\mathrm{orb},l}=\sum_{a,b}\epsilon_{lab}Q_ap_b$ the orbital angular momentum. Summing over the ordered pairs, the unit $\vec e_l$ and the cyclic factor give

$$
Q\longmapsto -2m\omega\sum_\eta L_{\mathrm{orb},\eta}\,i\vec e_\eta Q .
$$

Adding the two parts, the operator identity is

$$
\boxed{\;\mathcal{Q}_+\mathcal{Q}_-
= \vec p^{\,2} + m^2\omega^2\vec r^{\,2} -3\,\hbar\,m\,\omega - 2m\omega\sum_\eta  L_{\mathrm{orb},\eta}\,i\vec e_\eta\;}
$$

where the last term is the left multiplication by $i\vec e_\eta$ with the scalar $L_{\mathrm{orb},\eta}$ in front of it, and the second-order equation of the last section reads $(E^2-m^2c^4)\tilde{Ξ}_{\mathrm{sp},+}=c^2\mathcal{Q}_+\mathcal{Q}_-\tilde{Ξ}_{\mathrm{sp},+}$.

**Why the product is not the d'Alembertian.** The two factors are both pure vectors, so each is its own negative under the quaternion conjugate, and neither is the conjugate of the other. The product $\vec\nabla_-\vec\nabla_+$ is therefore not the norm of a single element, and its cross terms do not cancel as they do in $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Box$. They reduce instead to two remainders: the commutator $[Q_\eta,p_\eta]$, which is central and produces $-3\,\hbar\,m\,\omega$, and the antisymmetric part of the units' product, which produces $-2m\omega S$. That is the algebraic statement of the section's title: the product of the two first-order operators is central up to one vector term, and the vector term is the spin–orbit coupling. Nothing here rests on an anticommutation of actions; the anticommutation that matters is that of the three spatial units, which is part of the multiplication table.

**The two orders differ.** $\vec\nabla_+\vec\nabla_-$ is not $\vec\nabla_-\vec\nabla_+$, and the difference is in two places. The cross term of $\partial/\partial R_\eta$ with $Q_\eta$ changes sign with the order, so the constant changes sign: the order $\vec\nabla_+\vec\nabla_-$ gives $+3\,\hbar\,m\,\omega$ where the boxed identity has $-3\,\hbar\,m\,\omega$. The antisymmetric part of the coefficient changes sign with the order as well, so the spin–orbit term changes sign too. The two orders are therefore not related by an overall sign, and the boxed identity belongs to the order $\vec\nabla_-\vec\nabla_+$ alone. That is the order in which the substitution appears, the outer shift being the one carried by the line for $\tilde{Ξ}_{\mathrm{sp},+}$; its partner, $\hbar^{2}\,\vec \nabla_{+}\,\vec \nabla_{-}$, is the operator of the other supersymmetric member and carries $+3\,\hbar\,m\,\omega$ and $+2m\omega S$.

This is the load-bearing equation of the article. It was checked by exact differentiation on generic polynomial states of total degree at most three, with random complex coefficients: both sides were evaluated on the same state and the residual was zero, not merely small, because the differentiation of a polynomial is exact and no truncation enters. On that class of states the identity holds term by term, with integer coefficients on both sides. The commutator $[Q_\eta,p_\eta]=i\,\hbar$, which a truncated basis realises only in its bulk, is here an identity at every order, and it is the only place where $\hbar$ enters the product.

The right-hand side separates into three pieces. The first two terms are the **three-dimensional isotropic oscillator** in operator form,

$$
\vec p^{\,2} + m^2\omega^2\vec r^{\,2} = 2m\left(\frac{\vec p^{2}}{2\,m} + \tfrac12 m\omega^2\vec r^{\,2}\right) = 2m\,H_{\mathrm{osc}},
$$

with the standard spectrum $\hbar\,\omega\,(N+\tfrac32)$ in terms of the total oscillator number $N = 2n_r + l$. The constant $-3\,\hbar\,m\,\omega$ then removes exactly the zero-point energy of the oscillator, leaving $2\,\hbar\,m\,\omega N$. The last term is a **spin–orbit coupling** whose strength is tied to the oscillator frequency; it is not a small correction but a term of the same order as the level spacing, and it governs the whole spectral structure.

**Two values, and two only.** Write $S=\sum_\eta L_{\mathrm{orb},\eta}\,i\vec e_\eta$ for the last term without its coefficient. Since $(i\vec e_\eta)^2=e_t$ and $i\vec e_j$ anticommutes with $i\vec e_\eta$ for $j\ne k$, and since $(i\vec e_j)(i\vec e_\eta)=i\epsilon_{j\eta l}\,i\vec e_l$, the square of $S$ is

$$
S^2=\sum_\eta\bigl(L_{\mathrm{orb},\eta}\bigr)^2+\sum_{j<\eta}\bigl[L_{\mathrm{orb},j},L_{\mathrm{orb},\eta}\bigr]\,(i\vec e_j)(i\vec e_\eta)
= \vec L^{\,2}-\hbar\,S,
$$

where $[L_{\mathrm{orb},j},L_{\mathrm{orb},\eta}]=i\,\hbar\,\epsilon_{j\eta l}\,L_{\mathrm{orb},l}$. On a state of orbital number $l$ the operator $S$ therefore takes the two values $\hbar\,l$ and $-\hbar\,(l+1)$, the two roots of $\lambda^2=\hbar^{2}\,l\,(l+1)-\hbar\,\lambda$, and nothing else. The spin–orbit coupling is a two-valued operator, and that is the whole of its spectrum. The identity $S^2=\vec L^{\,2}-\hbar\,S$ was checked on generic polynomial states at residual zero.

## The Spectrum

Insert the boxed identity into the second-order equation:

$$
\left(E^2 - m^2c^4\right)\tilde{Ξ}_{\mathrm{sp},+}
= c^2\left(\vec p^{\,2} + m^2\omega^2\vec r^{\,2} -3\,\hbar\,m\,\omega - 2m\omega\,S\right)\tilde{Ξ}_{\mathrm{sp},+} .
$$

The first three terms are scalars in the position and in the orbital variables, while $S$ is diagonal in the basis of states of definite oscillator number $N$, definite $l$ and definite total angular momentum, and takes the two values above. The total angular momentum is the Hermitian element

$$
\tilde S_{\Psi,\mathrm{tot},\eta}=L_{\mathrm{orb},\eta}e_t+\tilde S_{\Psi,\eta},
\qquad
\tilde S_{\Psi,\eta}=\frac{\hbar}{2}i\vec e_\eta ,
$$

acting by left multiplication, and the contraction obeys $\sum_\eta(L_{\mathrm{orb},\eta}e_t)\tilde S_{\Psi,\eta}=\tfrac12(\tilde S_{\Psi,\mathrm{tot}}^2-\vec L^{\,2}-\tfrac34\hbar^{2}\,e_{t})$, so the two values of $S$ are read from the Casimir alone: $+\hbar\,l$ for $s_{\mathrm{tot}}=l+\tfrac12$ and $-\hbar\,(l+1)$ for $s_{\mathrm{tot}}=l-\tfrac12$. With $\vec p^{\,2} + m^2\omega^2\vec r^{\,2} -3\,\hbar\,m\,\omega =2\,\hbar\,m\,\omega N$ and $N = 2n_r + l$, and writing $\mathcal{S}=\frac{S}{\hbar}$ for the dimensionless value,

$$
\boxed{\;E^2 = m^2c^4 +2\,\hbar\,m\,\omega c^2\left(N - \mathcal{S}\right)
=
\begin{cases}
m^2c^4 +4\,\hbar\,m\,c^{2}\,\omega\,n_{r}, & s_{\mathrm{tot}} = l+\tfrac12, \\[4pt]
m^2c^4 +2\,\hbar\,m\,\omega c^2\left(2n_r + 2l + 1\right), & s_{\mathrm{tot}} = l-\tfrac12 .
\end{cases}\;}
$$

This is the Dirac-oscillator spectrum. Its structure is the two-branch pattern familiar from the literature: one branch is a tower in the radial quantum number $n_r$ alone, the other a tower shifted by the orbital quantum number; both are positive, so $E^2 \geq m^2c^4$ and the spectrum has a gap. The ground state has $n_r = 0$, $l = 0$, $s_{\mathrm{tot}} = \tfrac12$, and energy $E = \pm mc^2$; the first excited level stands at $E^2 = m^2c^4 +4\,\hbar\,m\,c^{2}\,\omega$.

The formula was also checked by direct diagonalisation of $H$ in a truncated oscillator basis, with $m=\hbar=\omega=c=1$ and the truncation $n_x+n_y+n_z\leq8$: the distinct values of $E^2$ that come out are $1$, $5$, $7$, $9$, $11$, $13$, $15$, $17$, $19$, $23$, $27$, $31$, $35$, which is the aligned tower $1+4n_r$ together with the anti-aligned tower $1+2(2n_r+2l+1)$ restricted to $l\geq1$. The value $3$ is absent because the anti-aligned branch needs $l\geq1$, and the values $21$, $25$, $29$ and $33$ because the aligned states that carry them need more than eight oscillator quanta. The lowest level $E^2=1$ comes out with the large multiplicity that the aligned branch predicts.

The $s_{\mathrm{tot}} = l+\tfrac12$ branch depends on $n_r$ and **not on $l$**. This is the characteristic degeneracy of the Dirac oscillator: for every $l$ with $s_{\mathrm{tot}} = l+\tfrac12$, the state with $n_r = 0$ has the same energy $E = \pm mc^2$, so the ground level is infinitely degenerate, and so is every other level of that branch, since $E^2$ there does not depend on $l$ at all. The degeneracy is not an artefact of the elimination of $\tilde{Ξ}_{\mathrm{sp},-}$ or of a particular gauge: it follows from the exact operator identity above, because the value $+\hbar\,l$ of $S$ cancels the orbital content of $N$ precisely for the aligned states. It is the same zero-mode structure that appears in the supersymmetric interpretation of the biquaternion section below, and it is the reason the model is called a "pseudo-oscillator": the spatial oscillator and the spin–orbit term conspire to produce a degeneracy pattern different from the non-relativistic oscillator's.

The anti-aligned case requires $l\geq1$, since $s_{\mathrm{tot}}=l-\tfrac12$ is a total angular momentum only for $l\geq1$; at $l=0$ the only state is the aligned one, with $s_{\mathrm{tot}}=\tfrac12$ and $S=0$.

The structure agrees with the published two-branch spectra obtained by solving the radial equations or by locating the poles of the Green's function (see the Further Reading); the derivation here obtains it directly from the operator identity, without a radial decomposition.

## The One-Dimensional Case

The one-dimensional oscillator shows the mechanism without the spin–orbit bookkeeping. With a single coordinate $Q$, the single two-sided action $\alpha:Q\mapsto\vec e_xQ\vec e_z$, the single shift $\vec e_x(\partial/\partial Q\pm\dfrac{\omega\,k_m}{c}Q)$ and the substitution $p \to p - im\omega\beta Q$, the pair reduces to

$$
(E-mc^2)\tilde{Ξ}_{\mathrm{sp},+} =i\,\hbar\,c\bigl(\partial/\partial Q+\frac{m\,\omega}{\hbar}Q\bigr)\tilde{Ξ}_{\mathrm{sp},-}\,\omega,
\qquad
(E+mc^2)\tilde{Ξ}_{\mathrm{sp},-} =i\,\hbar\,c\bigl(\partial/\partial Q-\frac{m\,\omega}{\hbar}Q\bigr)\tilde{Ξ}_{\mathrm{sp},+}\,\omega ,
$$

and the product of the two first-order operators is now a single element times a scalar operator, because $\omega^2=-e_t$ and there is no second spatial unit to carry a remainder:

$$\hbar^{2}\Bigl(\frac{\partial}{\partial Q}-\dfrac{\omega\,k_m}{c}Q\Bigr)\Bigl(\frac{\partial}{\partial Q}+\dfrac{\omega\,k_m}{c}Q\Bigr)
= -\bigl(p^2 + m^2\omega^2Q^2 -\hbar\,m\,\omega\bigr).
$$

The leading minus is not a convention. The two shifts are vector shifts, so the product carries the factor $\vec e_x\vec e_x=-e_t$, and the element product is

$$
\mathcal{Q}_+\mathcal{Q}_-
=\hbar^{2}\,\vec e_{x}\Bigl(\frac{\partial}{\partial Q}-\dfrac{\omega\,k_m}{c}Q\Bigr)\vec e_x\Bigl(\frac{\partial}{\partial Q}+\dfrac{\omega\,k_m}{c}Q\Bigr)
= p^2 + m^2\omega^2Q^2 -\hbar\,m\,\omega.
$$

The oscillator's zero point is $\tfrac12\hbar\,\omega$, so $p^2 + m^2\omega^2Q^2$ has eigenvalues $2\,\hbar\,m\,\omega(n+\tfrac12)$, and the constant removes the zero point exactly:

$$
\boxed{\;E^2 = m^2c^4 +2\,\hbar\,m\,\omega c^2\,n, \qquad n = 0,1,2,\dots\;}
$$

The spectrum is a single tower in $n$, and the ground state sits at $E = \pm mc^2$, as in the three-dimensional aligned branch but without the orbital multiplicity. The one-dimensional result is the cleanest check that the constant $-\hbar\,m\,\omega$ (which becomes $-3\,\hbar\,m\,\omega$ in three dimensions) is not a convention but a consequence of the commutator $[Q,p] =i\,\hbar$; the zero-point cancellation that produces the $E \propto n$ spectrum is the same mechanism in both cases. Both one-dimensional identities were checked on the monomials $Q^n$, $n=0,\dots,5$, at residual $0$: the scalar product gives the negated bracket, and the element product, which carries $\vec e_x\vec e_x=-e_t$, gives the bracket itself.

## The Non-Relativistic Limit and the Pseudo-Oscillator

The companion article on the Foldy–Wouthuysen transformation gives the systematic non-relativistic expansion. Applied to the oscillator it gives, on the large part, the effective operator $\mathcal{Q}_+\mathcal{Q}_-/(2m)$ — the leading order of $E-mc^2$ read off $E^2-m^2c^4=c^2\mathcal{Q}_+\mathcal{Q}_-$ — and its negative on the small part. The oscillator part of that operator is $\vec p^{\,2}/(2m)+\tfrac12m\omega^2\vec r^{\,2}$, whose levels would be $\hbar\,\omega\,(N+\tfrac32)$ if it were the whole of it.

It is not the whole operator. Divided by $2m$, the boxed identity gives

$$\frac{\mathcal{Q}_+\mathcal{Q}_-c}{2\,m\,c}
=\frac{\vec p^{2}}{2\,m}+\tfrac12m\omega^2\vec r^{\,2}-\tfrac32\hbar\,\omega-\omega\,S ,
$$

so the zero point is removed and a spin–orbit term of order $\omega$ is added, with no factor of $1/c^2$. Its two values are $-\hbar\,\omega\,l$ for $s_{\mathrm{tot}}=l+\tfrac12$ and $+\hbar\,\omega\,(l+1)$ for $s_{\mathrm{tot}}=l-\tfrac12$: both are of the order of the spacing $\hbar\,\omega$, and both grow with $l$. At leading order in $1/c$ the energy above the mass gap is therefore

$$
E-mc^2 \approx \hbar\,\omega\left(N-\mathcal{S}\right),
$$

which reproduces the two branches of the spectrum in the non-relativistic regime. Treating the spin–orbit term as a small perturbation of the non-relativistic oscillator is not legitimate: it is the same order as the level spacing, and it changes the degeneracy pattern. The non-relativistic limit of the Dirac oscillator is the oscillator **with a spin–orbit coupling of order $\omega$**, not the pure oscillator.

The comparison isolates where the relativistic content lives. In the free theory the spin–orbit coupling is a $1/c^2$ correction, because it comes from the elimination of the small part; in the oscillator it is present at leading order, because the confining substitution is itself linear in the position and frame-odd. The biquaternion framework reads this as the statement that the substitution shifts the **odd** part of the operator, and the odd part is precisely what the product converts into an even operator with a spin–orbit component.

## The Biquaternion Reading

Three structural statements can now be made in the algebra.

**The substitution is a shift of the odd part.** The gradient $\tilde\nabla=e_t\,\partial/\partial R_t+\sum_\eta\vec e_\eta\,\partial/\partial R_\eta$ has a frame-even part ($e_t\,\partial/\partial R_t$, the timelike direction) and a frame-odd part ($\sum_\eta\vec e_\eta\,\partial/\partial R_\eta$, the spacelike directions). What the substitution adds to the operator is the action $\tilde{Ξ}_{\mathrm{sp}}\mapsto-cm\omega\sum_\eta\vec e_\eta\,(Q_\eta\tilde{Ξ}_{\mathrm{sp}})\,\vec e_y$, and that action is frame-odd, since it anticommutes with $\beta$; it is also linear in the position. Multiplying the two first-order operators of the pair returns a second-order operator that is central except for one remainder: the pieces built from the two shifted gradients combine as in the free case, and what survives beside the centre is the spin–orbit part. In the elements it is

$$
-2m\omega\,S=-2m\omega\sum_\eta  L_{\mathrm{orb},\eta}\,i\vec e_\eta
\;\longleftrightarrow\;
-\dfrac{4\omega\,k_m}{c}\sum_\eta\bigl(L_{\mathrm{orb},\eta}e_t\bigr)\tilde S_{\Psi,\eta} ,
\qquad
\tilde S_{\Psi,\eta}=\frac{\hbar}{2}i\vec e_\eta ,
$$

a Hermitian element of $\mathbb{B}_{\Psi}$: $i\vec e_\eta$ is Hermitian, $L_{\mathrm{orb},\eta}$ is Hermitian, and the two commute. The spin is the Hermitian element $i\vec e_\eta$, the orbital angular momentum is the scalar operator $L_{\mathrm{orb},\eta}$, and the coupling is their contraction, which is the operator $\sum_\eta L_{\mathrm{orb},\eta}\tilde S_{\Psi,\eta}$ of the hydrogen article up to the factor $-\frac{4\,m\,\omega}{\hbar}$. That the remainder is Hermitian and not central is the algebraic statement that the oscillator's product is not the Klein–Gordon operator: the non-minimal term, unlike the mass, does not merely shift the eigenvalue, it adds a Hermitian element to the product.

**The zero point is a commutator.** The constant $-3\,\hbar\,m\,\omega$ comes from the commutator of position and momentum. The shift carries $\vec e_\eta\,(Q_\eta\tilde{Ξ}_{\mathrm{sp}})\,\vec e_y$ against the momentum $p_\eta$, and the two do not commute: their commutator is the central scalar $[Q_\eta,p_\eta]=i\,\hbar$, and the sum over the three directions is $3\,i\,\hbar$. The factor $im\omega$ of the substitution turns it into $-3\,\hbar\,m\,\omega$ through one use of $i^2=-1$. This is why the aligned ground state sits at the mass gap: the commutator has removed the zero-point energy exactly, and the cancellation counts the number of spatial directions rather than any particular representation.

**The zero modes are supersymmetric.** The operator identity has the form of a factorisation, $\mathcal{Q}_+\mathcal{Q}_-$ with the conjugate pair of *The Square of the Coupled Operator*. The aligned states with $n_r=0$ are exactly the **zero modes** $\mathcal{Q}_-\tilde{Ξ}_{\mathrm{sp},+}=0$, and their infinite degeneracy is the zero-mode degeneracy of the factorised operator. The pair $(\mathcal{Q}_-,\mathcal{Q}_+)$ is the standard supersymmetric pair of quantum physics: $\mathcal{Q}_+\mathcal{Q}_-$ and $\mathcal{Q}_-\mathcal{Q}_+$ are partner Hamiltonians, and the zero modes of one are the states the supersymmetry relates. That this supersymmetry is present, and hidden in the Dirac equation rather than imposed, is the content of the Benítez–Salas-Brito solution listed in the Further Reading. The companion article *Supersymmetric Quantum Physics in the Biquaternion Framework* develops this correspondence; the Dirac oscillator is its exactly solvable relativistic realisation. The two operators here are not the two gradients $\tilde\nabla_\Phi,(\tilde\nabla_\Phi)^{\natural}$ of the free mass pair but their shifted, frame-projected forms; what is common to both is that the product of a first-order operator with its conjugate partner is a second-order operator whose zero modes carry the structure.

### The gap is not closed

**The identity says the spectrum is gapped, and it says it for every frequency.** The right-hand side of the boxed identity is $\vec p^{\,2}+m^{2}\omega^{2}\vec r^{\,2}-3\,\hbar\,m\,\omega-2m\omega S$, and its lowest eigenvalue is zero, attained on the aligned states with $n_r=0$; that is the zero-point cancellation of the previous paragraph, read as a statement about the operator rather than about a level. Hence $\mathcal{Q}_+\mathcal{Q}_-\ge0$, and since $E^{2}-m^{2}c^{4}=c^{2}\mathcal{Q}_+\mathcal{Q}_-$,

$$
E^{2}\ge m^{2}c^{4}\quad\text{for every level, at every oscillator frequency} ,
$$

so the positive branch begins at $mc^{2}$, the negative branch ends at $-mc^{2}$, and no level ever lies strictly inside the gap. The spectrum written above, $E^{2}=m^{2}c^{4}+4\,\hbar\,m\,c^{2}\,\omega\,n_r$ on the aligned branch, is the same statement term by term. The oscillator is therefore **Klein-stable**: no strength of confinement, at any frequency, produces a pair, because no level can reach $E=0$ and none can reach the lower edge of the gap from inside.

**Why the stability is a property of the side and not of the strength.** The mass shell of the free pair is one equation, written with its two sides apart,

$$
\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_m^{2}
\qquad\Longleftrightarrow\qquad
k_{t}^{\prime\,2}=k_{\Phi}^{2}+k_m^{2},
\qquad
k_{t}^{\prime}=\frac{E}{\hbar\,c},
\qquad
k_{\Phi}=\frac{p}{\hbar},
$$

the temporal coefficient on the left and the spatial part on the right. The oscillator's substitution acts on the spatial part and on nothing else, as the paragraph *The shift of the gradient* states: $\vec p\mapsto\vec p-im\omega\beta\vec r$ is a shift of $\vec\nabla$, and the two opposite shifts $\vec\nabla_{\pm}$ supply the diagonal term $+m^{2}\omega^{2}\vec r^{\,2}$ of the boxed identity, since the raw product of the shifts, $-\omega^{2}m^{2}\vec r^{\,2}$, is flipped by the overall sign. The confining term is therefore an addition to the right-hand side, positive when the oscillator frequency is positive, and it pushes every level away from the gap. An electrostatic potential does the opposite thing in the opposite place: it is the central shift $D=\tilde\nabla_\Phi-\frac{ϙ\,a'_{t}}{\hbar}e_t$, so it moves $k_{t}^{\prime}$ by a real amount and drags the level down until it reaches $-mc^{2}$. That is the Klein step of the companion article, and its bounded form is the well whose lowest level dives at $V_0^{\mathrm{cr}}=mc^{2}[1+\sqrt{1+(n_{\mathrm{w}}\pi/(k_mL))^{2}}\,]$, as computed in *Pair Creation in a Bounded Region in Biquaternionic Form*.

**The three confinements.** A step in the mass is the third case, and it is stable for the oscillator's reason: the mass is the chirality-mixing term, a change of it shifts no frequency, so the transmitted wave is evanescent and there is no threshold; that is the bag-model mechanism of Bardeen, Chanowitz, Drell, Weinstein and Yan, used precisely because it has no Klein threshold. Two of the three confinements are stable and one is not, and the reading is uniform: the confining term that acts off the temporal coefficient cannot create pairs, and the one that acts on it can. The oscillator has been the corpus's model of relativistic confinement, and this reading adds what the model's spectrum already implies: its confinement is of the stable kind, and the exact solvability and the pair stability are two faces of the same substitution.

## Summary

The Dirac oscillator is the system obtained by the non-minimal substitution $\vec p \to \vec p - im\omega\beta\vec r$ in the Dirac Hamiltonian. The substitution is frame-odd, imaginary and linear in the position; it shifts the odd part of the first-order operator without touching the even (mass) part. A state is an element $\tilde{Ξ}_{\mathrm{sp}}$ of $\mathbb{B}$, the frame action $\beta$ splits it uniquely into $\tilde{Ξ}_{\mathrm{sp},+}$ and $\tilde{Ξ}_{\mathrm{sp},-}$, and the equation is the pair

$$
(E-mc^2)\tilde{Ξ}_{\mathrm{sp},+} =i\,\hbar\,c\bigl(\vec\nabla_+\tilde{Ξ}_{\mathrm{sp},-}\bigr)\omega,
\qquad
(E+mc^2)\tilde{Ξ}_{\mathrm{sp},-} =i\,\hbar\,c\bigl(\vec\nabla_-\tilde{Ξ}_{\mathrm{sp},+}\bigr)\omega,
\qquad
\omega=-\vec e_z .
$$

Eliminating $\tilde{Ξ}_{\mathrm{sp},-}$ and multiplying the two shifted gradients, with the multiplication table of the three spatial units together with $[Q_\eta,p_\eta]=i\,\hbar$, gives the exact operator identity, with $\mathcal{Q}_\pm$ the conjugate pair of *The Square of the Coupled Operator*,

$$
\boxed{\;\mathcal{Q}_+\mathcal{Q}_-
= \vec p^{\,2} + m^2\omega^2\vec r^{\,2} -3\,\hbar\,m\,\omega - 2m\omega\sum_\eta  L_{\mathrm{orb},\eta}\,i\vec e_\eta\;}
$$

checked by exact differentiation on generic polynomial states, with residual zero. The right-hand side is the three-dimensional oscillator with its zero point removed, plus a spin–orbit coupling of order $\omega$; the coupling is the element $S=\sum_\eta L_{\mathrm{orb},\eta}i\vec e_\eta$, which takes the two values $\hbar\,l$ and $-\hbar\,(l+1)$ because $S^2=\vec L^{\,2}-\hbar\,S$. The spectrum is

$$
E^2 = m^2c^4 +2\,\hbar\,m\,\omega c^2\left(N - \mathcal  S\right)
=
\begin{cases}
m^2c^4 +4\,\hbar\,m\,c^{2}\,\omega\,n_{r}, & s_{\mathrm{tot}} = l+\tfrac12, \\[4pt]
m^2c^4 +2\,\hbar\,m\,\omega c^2\left(2n_r+2l+1\right), & s_{\mathrm{tot}} = l-\tfrac12,
\end{cases}
$$

with the aligned branch independent of $l$ and hence an infinitely degenerate level at $E = \pm mc^2$. In one dimension the spin–orbit term is absent and the spectrum is $E^2 = m^2c^4 +2\,\hbar\,m\,\omega c^2 n$, $n = 0,1,2,\dots$.

In the biquaternion framework the substitution shifts the frame-odd part of the gradient, and in the actions its imaginary coefficient is spent on the action: the added term is $\tilde{Ξ}_{\mathrm{sp}}\mapsto-cm\omega\sum_\eta\vec e_\eta\,(Q_\eta\tilde{Ξ}_{\mathrm{sp}})\,\vec e_y$, a real coefficient times a Hermitian, frame-odd action. The product is central except for the Hermitian remainder $-2m\omega\sum_\eta L_{\mathrm{orb},\eta}i\vec e_\eta$, which in the elements is $-\dfrac{4\omega\,k_m}{c}\sum_\eta(L_{\mathrm{orb},\eta}e_t)\tilde S_{\Psi,\eta}$. The zero-point cancellation is the sum of the commutator $[Q_\eta,p_\eta]=i\,\hbar$ over the three spatial directions, converted to $-3\,\hbar\,m\,\omega$ by one factor $i^2=-1$. The zero modes of the shifted operator are the supersymmetric partner structure that the companion article develops. One field never carries the mass: the mass needs the pair, because $\tilde\nabla^2$ is not scalar, and the whole derivation uses the one gradient and its two shifts, with no matrix, no array and no Clifford generator. The spectrum also settles the question of what this confinement can do to the vacuum: since $\mathcal{Q}_+\mathcal{Q}_-\ge0$, the gap is empty at every frequency and the model cannot create pairs, whereas an electrostatic well can, once its depth passes the threshold of *Pair Creation in a Bounded Region in Biquaternionic Form*. The stability and the exact solvability are two consequences of the one substitution.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{B}_{\Psi}$ | Hermitian (informational) sector |
| $\mathbb{B}_{\Phi}$ | Material sector, with $Q_t=i q'_t$ and $\partial/\partial R_t=-i\,\partial/\partial r'_t$ |
| $e_t = 1$, $\vec e_x, \vec e_y, \vec e_z$ | Quaternion units, $\vec e_\eta^2 = -e_t$, $\vec e_y\vec e_x = -\vec e_z$ |
| $\tilde\nabla_\Phi$ | The corpus gradient, $e_t\,\partial/\partial R_t+\vec e_x\,\partial/\partial R_x+\vec e_y\,\partial/\partial R_y+\vec e_z\,\partial/\partial R_z$ |
| $(\tilde\nabla_\Phi)^{\natural}$ | Its quaternion conjugate, with $\varepsilon=(1,-1,-1,-1)$ |
| $\Box = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= \partial^2/\partial R_t^2+\Delta_Q$ | The d'Alembertian; on $\mathbb{B}_{\Phi}$, $\Delta-\partial^2/\partial {r'_t}^2$ |
| $\vec\nabla = \sum_\eta\vec e_\eta\,\partial/\partial R_\eta$ | Spatial part of the gradient; $\vec\nabla\vec\nabla = -\Delta_Q$ |
| $\vec\nabla_\pm = \vec\nabla\pm\dfrac{\omega\,k_m}{c}\vec r$ | The two non-minimal shifts of the spatial gradient |
| $\omega = -\vec e_z$, $\omega^2=-e_t$ | The pseudoscalar; the right factor carried by a velocity action |
| $Q\mapsto aQb$ | Action on a state; the two-sided multiplication, written out |
| $\beta:\ Q\mapsto iQ\vec e_x$ | Frame action; the single right action by $i\vec e_x$; $\beta^2=\mathrm I$ |
| $\alpha_\eta:\ Q\mapsto \vec e_\eta Q\vec e_z$ | Velocity actions; two-sided, with the elements $\vec e_\eta$ and $\vec e_z$; Hermitian, $\alpha_\eta^2=\mathrm I$ |
| $\beta\alpha_\eta:\ Q\mapsto i\vec e_\eta Q\vec e_y$, $\alpha_\eta\beta:\ Q\mapsto-i\vec e_\eta Q\vec e_y$ | The two mixed products; $\beta\alpha_\eta\beta=-\alpha_\eta$ |
| $Q_L$, $Q_R$ | The two components of the pair, named $L$ and $R$ |
| $H = c\sum_\eta\alpha_\eta(p_\eta-im\omega\beta Q_\eta) + \beta mc^2$ | Dirac-oscillator Hamiltonian, the source's equation |
| $p_\eta=-i\,\hbar\partial/\partial R_\eta$, $\vec p=\sum_\eta\vec e_\eta p_\eta$ | Corpus momentum operator, the spatial gradient in disguise |
| $\vec p - im\omega\beta\vec r$ | Non-minimal substitution, the frame-odd shift |
| $\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L}$, $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$ | The pair, as two first-order lines on a pair of elements of $\mathbb{B}$; each line composed with its partner is $\Box$ |
| $\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L}$, $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$ | The chiral pair, $k_m=mc/\hbar$ |
| $\tilde{Ξ}_{\mathrm{sp},+}$, $\tilde{Ξ}_{\mathrm{sp},-}$ | The two frame parts, $\beta\tilde{Ξ}_{\mathrm{sp},\pm}=\pm\tilde{Ξ}_{\mathrm{sp},\pm}$; large and small |
| $\mathcal{Q}_\pm:\ \tilde{Ξ}_{\mathrm{sp}}\mapsto i\,\hbar\,\vec \nabla_{\mp}\,\tilde{Ξ}_{\mathrm{sp}}\,\omega$ | Factorised conjugate actions; $\mathcal{Q}_+\mathcal{Q}_-=\hbar^{2}\,\vec \nabla_{-}\,\vec \nabla_{+}$ |
| $\mathcal{Q}_+\mathcal{Q}_- = \vec p^{\,2}+m^2\omega^2\vec r^{\,2}-3\,\hbar\,m\,\omega-2m\omega S$ | Operator identity |
| $S = \sum_\eta L_{\mathrm{orb},\eta}\,i\vec e_\eta$ | Spin–orbit element, Hermitian; $S^2=\vec L^{\,2}-\hbar\,S$ |
| $\tilde S_{\Psi,\eta} =\frac{\hbar}{2}i\vec e_\eta$, $\tilde S_{\Psi,\mathrm{tot},\eta}=L_{\mathrm{orb},\eta}e_t+\tilde S_{\Psi,\eta}$ | Spin and total angular momentum elements |
| $\mathcal  S =\frac{S}{\hbar}$ | Dimensionless value of the spin–orbit element |
| $\vec L = \vec r\times\vec p$, $L_{\mathrm{orb},\eta}=\sum_{a,b}\epsilon_{\eta ab}Q_ap_b$ | Orbital angular momentum |
| $N = 2n_r + l$ | Total oscillator quantum number |
| $n_r$ | Radial quantum number |
| $E^2 = m^2c^4+4\,\hbar\,m\,c^{2}\,\omega\,n_{r}$ ($s_{\mathrm{tot}}=l+\tfrac12$) | Aligned branch |
| $E^2 = m^2c^4+2\,\hbar\,m\,\omega c^2(2n_r+2l+1)$ ($s_{\mathrm{tot}}=l-\tfrac12$) | Anti-aligned branch |
| $E^2 = m^2c^4+2\,\hbar\,m\,\omega c^2 n$ | One-dimensional spectrum |

## Further Reading

- M. Moshinsky and A. Szczepaniak, "The Dirac oscillator," *Journal of Physics A: Mathematical and General* **22** (1989) L817–L819, for the original non-minimal substitution and the exact solution.
- M. Moshinsky and Yu. F. Smirnov, *The Harmonic Oscillator in Modern Physics* (Harwood, 1996), for the oscillator algebra, the pseudo-oscillator, and the relativistic realisation.
- A. D. Alhaidari, "The Dirac-oscillator Green's function," *International Journal of Theoretical Physics* **43** (2004) 939–946, for the two-branch energy spectrum obtained from the Green's-function poles.
- J. Benítez, R. P. Martínez y Romero, H. N. Núñez-Yépez and A. L. Salas-Brito, "Solution and hidden supersymmetry of a Dirac oscillator," *Physical Review Letters* **64** (1990) 1643–1645 (erratum **65** (1990) 2085), for the hidden supersymmetry that the zero-mode discussion reproduces.
- R. Szmytkowski and M. Gruchowski, "Completeness of the Dirac oscillator eigenfunctions," *Journal of Physics A: Mathematical and General* **34** (2001) 4991–4997, for the completeness of the two-branch eigenfunctions.
- P. Strange and L. H. Ryder, "The Dirac oscillator in a rotating frame of reference," *Physics Letters A* **380** (2016) 3465–3468, for the oscillator in a non-inertial setting and the subtleties the rotation introduces.
- F. Domínguez-Adame and M. A. González, "Solvable linear potentials in the Dirac equation," *Europhysics Letters* **13** (1990) 193–198, for the linear — oscillator — potential solved in reduced dimensions.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the Dirac representation, the coupled two-spinor equations and the non-relativistic reduction.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the Dirac Hamiltonian and the Foldy–Wouthuysen reduction used in the non-relativistic comparison.
