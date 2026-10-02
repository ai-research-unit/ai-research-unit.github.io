# __Noether's Two Theorems__

## Introduction

A symmetry of an action produces a conservation law. That sentence is usually called Noether's theorem, and it is the wrong statement of it. There are two theorems, they apply to two different kinds of symmetry, and only the first returns a conservation law. The first theorem applies to a symmetry whose parameters are **constants** — finitely many of them — and gives one conservation law for each parameter. The second applies to a symmetry whose parameters are **arbitrary functions of the coordinates** — infinitely many of them — and gives no new conservation law at all: it gives a differential **identity** satisfied by the equations of motion, from which it follows that those equations are not independent.

The two kinds of symmetry look alike on the page, and that is the source of the error the second theorem corrects. A rigid rotation and a rotation by an angle that varies from point to point are written with the same symbol, and the local one can be misread as an infinite family of rigid ones, each with its own conserved charge. It is not. The local symmetry is a smaller amount of information about the *solutions*, not a larger amount: it says that the equations are degenerate, and degeneracy is a constraint on the system rather than a supply of integrals.

The terminology is Hermann Weyl's, and it is easy to reverse. A symmetry of the **first kind** is rigid: its parameters are constants. A symmetry of the **second kind** is local: its parameters are functions of the coordinates. Weyl introduced the names in 1918, in the paper on gravitation and electricity, in the same year as Noether's paper, and they have survived with frequent inversion — a local transformation is often met under the name "of the first kind", which is exactly backwards. The naming is fixed below.

Two consequences of the second theorem organise every field theory that carries a local symmetry. First, the field equations are subject to identities, so the number of independent equations is smaller than the number of equations, and a gauge condition must be added before the initial-value problem is well posed. Second, the identity constrains the source: when the equations are sourced, the divergence of the identity forces the source to be conserved, and the conservation of the charge is then an **integrability condition** on the equations rather than an independent law.

The article is confined to a Lagrangian field theory with finitely many fields on flat spacetime, which is the setting in which the two theorems are used in this series. It first fixes the fundamental variation identity from which both theorems follow, then derives the first theorem and its current, then proves the second theorem and reads what it says, then works the two standard examples — the Maxwell field, whose local symmetry is a pure one of the second kind, and a Stueckelberg-type field, whose local symmetry contains a rigid subgroup — then counts the conservation laws against the identities, and closes with the relation to the Hamiltonian form and with the naming.

## The Setting and the Fundamental Identity

**Definition.** The fields are $u^1,\dots,u^N$, functions of the coordinates $x^0,\dots,x^{m-1}$ of flat spacetime with coordinates written $x^\mu$ and partial derivatives written $\partial_\mu$. The **Lagrangian density** is a function $L(x,u,\partial u)$ of the coordinates, the fields and their first derivatives, and the **action** is the functional

$$
S[u] = \int_\Omega L\bigl(x,u(x),\partial u(x)\bigr)\,d^mx .
$$

**Definition.** The **Euler–Lagrange expression** of the $i$-th field is

$$
E_i = \frac{\partial L}{\partial u^i} - \partial_\mu\frac{\partial L}{\partial u^i_{,\mu}} ,
$$

abbreviated $L^\mu_i = \partial L/\partial u^i_{,\mu}$ for the derivative with respect to the gradient. A field configuration is **on shell** when $E_i=0$ for every $i$, and **off shell** otherwise.

**Theorem (the fundamental variation identity).** For any variation $\delta u^i$, the variation of the density is

$$
\delta L = E_i\,\delta u^i + \partial_\mu\Theta^\mu ,
\qquad
\Theta^\mu = L^\mu_i\,\delta u^i .
$$

*Proof.* Expanding the variation and inserting the definition of $E_i$,

$$
\delta L = \frac{\partial L}{\partial u^i}\delta u^i + L^\mu_i\,\partial_\mu\delta u^i
= \Bigl(\frac{\partial L}{\partial u^i} - \partial_\mu L^\mu_i\Bigr)\delta u^i + \partial_\mu\bigl(L^\mu_i\,\delta u^i\bigr),
$$

which is the stated identity. ∎

The identity splits the change of the density into a piece that vanishes on shell — the equations of motion contracted with the variation — and a piece that is a divergence, the boundary current $\Theta^\mu$. Everything below is that identity read with a different kind of variation.

**Stationarity.** Integrating the identity over $\Omega$ and requiring $S$ to be stationary under variations vanishing on the boundary gives $\int E_i\delta u^i=0$ for every such variation, hence $E_i=0$ by the fundamental lemma of the calculus of variations. If the variation does not vanish on the boundary, the boundary term $\oint\Theta^\mu\,d\Sigma_\mu$ is the natural boundary condition. The variational derivation is the subject of *The Calculus of Variations*; what is added here is the classification of the symmetries.

**Definition.** A variation is a **symmetry of the action up to a divergence** when the density changes by a divergence,

$$
\delta L = \partial_\mu F^\mu ,
$$

for some $F^\mu$ depending on the fields and the variation. The divergence is allowed because it does not change the equations of motion: the two densities differ by a boundary term, and both give the same $E_i$.

## The First Theorem

**Definition.** A **symmetry of the first kind**, or rigid symmetry, is a symmetry whose transformation is a one-parameter family,

$$
\delta_\alpha u^i = \alpha\,\xi^i(x,u,\partial u) ,
$$

with the parameter $\alpha$ a **constant**, and with $\delta_\alpha L = \alpha\,\partial_\mu F^\mu$ a divergence. A symmetry depending on $k$ independent constant parameters $\alpha^1,\dots,\alpha^k$ is written as a sum $\delta u^i = \xi^i_a\epsilon^a$, with a repeated index summed over $a=1,\dots,k$.

**Theorem (Noether, first theorem).** Let $\delta u^i = \alpha\,\xi^i$ be a symmetry of the first kind, with $\delta L = \alpha\,\partial_\mu F^\mu$. Then the field

$$
j^\mu = L^\mu_i\,\xi^i - F^\mu
$$

satisfies

$$
\partial_\mu j^\mu = -\,E_i\,\xi^i ,
$$

and is therefore conserved, $\partial_\mu j^\mu=0$, on every solution of the equations of motion. For a $k$-parameter group the construction gives $k$ currents $j^\mu_a = L^\mu_i\xi^i_a - F^\mu_a$.

*Proof.* The fundamental identity for the variation $\delta u^i = \alpha\xi^i$ reads

$$
\alpha\,\partial_\mu F^\mu = \alpha\,E_i\xi^i + \alpha\,\partial_\mu\bigl(L^\mu_i\xi^i\bigr),
$$

and cancelling the common factor $\alpha$ gives $E_i\xi^i = \partial_\mu(F^\mu - L^\mu_i\xi^i) = -\partial_\mu j^\mu$. ∎

**The conserved charge.** If the current falls off fast enough at spatial infinity, the **Noether charge**

$$
Q = \int j^0\,d^{m-1}x
$$

is constant in time, because $\frac{d}{dt}Q = \int\partial_0j^0\,d^{m-1}x = -\int\partial_kj^k\,d^{m-1}x$ vanishes as a boundary term.

### Worked Examples of the First Theorem

**Translation invariance and the energy–momentum tensor.** Let the density contain no explicit dependence on the coordinates and let the fields transform with the coordinates, $\delta u^i = \xi^\nu\partial_\nu u^i$ under $x^\mu\mapsto x^\mu+\xi^\mu$ with $\xi^\mu$ constant. Then $\delta L = \xi^\nu\partial_\nu L = \partial_\nu(\xi^\nu L)$, so $F^\mu=\xi^\mu L$, and

$$
j^\mu = L^\mu_i\,\xi^\nu\partial_\nu u^i - \xi^\mu L = \xi^\nu\,T^\mu{}_\nu ,
\qquad
T^\mu{}_\nu = L^\mu_i\,\partial_\nu u^i - \delta^\mu_\nu\,L .
$$

The four conserved quantities are the components of the four-momentum, and $T^\mu{}_\nu$ is the **canonical energy–momentum tensor**. It is conserved on shell, $\partial_\mu T^\mu{}_\nu=0$, and it need not be symmetric; the symmetric tensor of the field-theoretic account is an improvement of it by a superpotential, which alters neither the conservation law nor the total charge.

**Lorentz invariance and angular momentum.** For the Lorentz group the parameter is instead the constant antisymmetric pair $\omega_{\mu\nu}$, the fields transform by their Lorentz action plus the coordinate change, and the six conserved quantities are the components of the angular-momentum tensor. The counting is the only point needed here: the group has $k=6$ parameters and the first theorem returns $6$ conservation laws.

**An internal symmetry and the electric-type current.** Let the density be invariant under the constant phase rotation of a complex field, $\delta\phi = i\alpha\phi$, $\delta\phi^* = -i\alpha\phi^*$. For the massless complex scalar with

$$
L = \partial_\mu\phi^*\,\partial^\mu\phi ,
$$

the conjugate momentum is $L^\mu_\phi = \partial^\mu\phi^*$ and $L^\mu_{\bar{\phi}} = \partial^\mu\phi$, so the current is

$$
j^\mu = i\bigl(\phi\,\partial^\mu\phi^* - \bar{\phi}\partial^\mu\phi\bigr).
$$

Its divergence computed off shell is

$$
\partial_\mu j^\mu = i\bigl(\phi\,\Box\phi^* - \bar{\phi}\Box\phi\bigr),
$$

which is precisely $-E_\phi\xi^\phi - E_{\bar{\phi}}\xi^{\bar{\phi}}$ and therefore vanishes on shell. The identity was checked on a superposition of two on-shell plane waves with null wave vectors, where the divergence is $2.2\times10^{-13}$. This current is the ancestor of the electric four-current of a complex field, and the corpus's *Noether's Theorem in Biquaternionic Form* carries its biquaternion image, the material-sector current $\tilde{J}$.

## The Second Theorem

The second theorem is what happens when the parameter is not a constant.

**Definition.** A **symmetry of the second kind**, or local symmetry, is a symmetry whose transformation depends on $q$ arbitrary functions $\varepsilon^\alpha(x)$ of the coordinates and their derivatives,

$$
\delta u^i = \sum_{\alpha=1}^{q}\Bigl(a^{i\mu}_\alpha(x,u)\,\partial_\mu\varepsilon^\alpha + b^i_\alpha(x,u)\,\varepsilon^\alpha\Bigr) ,
$$

with the action invariant up to a divergence, $\delta L = \partial_\mu F^\mu$, **for every choice of the functions** $\varepsilon^\alpha$. When the transformation law contains derivatives of $\varepsilon$ up to order $r$, the coefficient of the highest derivative is written $a^{i\mu_1\cdots\mu_k}_\alpha$ for $k\le r$, and $a^{i\varnothing}_\alpha = b^i_\alpha$.

**Theorem (Noether, second theorem).** Let the action admit a symmetry of the second kind depending on the $q$ arbitrary functions $\varepsilon^\alpha$. Then the Euler–Lagrange expressions satisfy, **identically in the fields and off shell**, the $q$ differential identities

$$
\sum_{i}\sum_{k=0}^{r}(-1)^k\,\partial_{\mu_1}\cdots\partial_{\mu_k}\Bigl(a^{i\mu_1\cdots\mu_k}_\alpha\,E_i\Bigr) \equiv 0 ,
\qquad \alpha = 1,\dots,q ,
$$

with $a^{i\varnothing}_\alpha = b^i_\alpha$. In particular, when the transformation is first order in $\varepsilon$, the identity is

$$
b^i\,E_i - \partial_\mu\bigl(a^{i\mu}E_i\bigr) \equiv 0 .
$$

*Proof.* Integrate the left side of the fundamental identity against the symmetry variation over all of spacetime, with the functions $\varepsilon^\alpha$ of compact support so that all boundary terms vanish. Since $\delta L$ is a divergence, the integral of $\delta L$ vanishes, and the fundamental identity gives

$$
0 = \int E_i\,\delta u^i\,d^mx
= \int\Bigl[b^i_\alpha E_i\,\varepsilon^\alpha + a^{i\mu}_\alpha E_i\,\partial_\mu\varepsilon^\alpha\Bigr]d^mx ,
$$

with the sum over $\alpha$ and the repeated index $i$ understood. Integrating the second term by parts — no boundary term arises, the support of $\varepsilon^\alpha$ being compact — gives

$$
\int\Bigl(b^i_\alpha E_i - \partial_\mu\bigl(a^{i\mu}_\alpha E_i\bigr)\Bigr)\varepsilon^\alpha\,d^mx = 0 ,
$$

for every compactly supported $\varepsilon^\alpha$. The fundamental lemma then gives the stated identity for each $\alpha$. The higher-order form follows by integrating by parts $k$ times, at each step producing the factor $(-1)^k$. ∎

Three features of the theorem are worth stating before the examples, because each is a place where the first theorem is misapplied.

**The identity is off shell.** It holds whether or not the fields solve the equations, and on the solutions both sides vanish trivially, since every term carries an $E_i$. It is therefore not a conservation law: it supplies no quantity that is constant for the solutions, because it is empty for the solutions. What it supplies is a relation between the components of the equations.

**It says the equations are not independent.** If the $N$ fields are subject to $q$ identities of the second kind, then at most $N-q$ of the equations are independent. The system is degenerate; the solution set is a union of orbits of the local symmetry, and a gauge condition — a further condition that selects one representative from each orbit — is needed before a unique evolution is determined by initial data.

**It makes the local symmetry carry no charge.** A local symmetry generally contains no rigid subgroup, because a transformation whose parameter is a function $\varepsilon(x)$ need not survive when $\varepsilon$ is restricted to a constant. When it does survive — when the algebraic part $b^i_\alpha$ is nonzero — the rigid subgroup is a genuine first-kind symmetry and has its own conservation law, and the $\varepsilon$-coefficient of the identity is the statement that a certain total divergence vanishes off shell: the rigid current corrected by the term $a^{i\mu}_\alpha E_i$. That remark is made precise in the Stueckelberg example below. But when $b^i_\alpha$ vanishes, the local symmetry has no rigid subgroup and produces no conservation law whatsoever. This is the case for the Maxwell field, and it is the reason a gauge transformation is not a source of new charges.

## Worked Example: the Maxwell Field

The Maxwell field is the original illustration of the second theorem and the one the corpus uses.

**The variational problem.** Let the field be the four-potential $A_\nu$ and the density be

$$
L = -\tfrac14 F_{\mu\nu}F^{\mu\nu} ,
\qquad
F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu .
$$

The Euler–Lagrange expression is

$$
E^\nu = \frac{\partial L}{\partial A_\nu} - \partial_\mu\frac{\partial L}{\partial(\partial_\mu A_\nu)} = \partial_\mu F^{\mu\nu} ,
$$

the source-free side of the inhomogeneous Maxwell equations.

**The local symmetry.** The transformation $A_\nu\mapsto A_\nu+\partial_\nu\varepsilon$ leaves $F_{\mu\nu}$, and hence the density, exactly invariant: $F$ is unchanged, so $\delta L = 0$ and $F^\mu=0$ in the notation above. In the standard form the transformation is $\delta A_\nu = a_{\nu}{}^{\mu}\partial_\mu\varepsilon$ with $a_\nu{}^\mu = \delta_\nu{}^\mu$ and $b_\nu=0$. The parameters are the four functions $A_\nu$ and the arbitrary function $\varepsilon$, so $q=1$, and the algebraic part vanishes. The symmetry is a pure second-kind symmetry with no rigid subgroup.

**The identity.** Substituting into the theorem, with $b=0$ and $a_\nu{}^\mu=\delta_\nu{}^\mu$,

$$
-\,\partial_\mu\bigl(\delta_\nu{}^\mu E^\nu\bigr) = -\,\partial_\nu E^\nu \equiv 0 ,
$$

that is,

$$
\partial_\nu\partial_\mu F^{\mu\nu} \equiv 0 ,
$$

which is the antisymmetry of $F^{\mu\nu}$ contracted with the symmetric pair $\partial_\nu\partial_\mu$. The identity was checked on a random smooth off-shell potential by finite differences, with residual exactly $0$ against a scale of $2$.

**What the identity does.** The four equations $E^\nu=0$ are subject to one identity, so only three are independent. In the $3+1$ split the time component $\nu=0$ is Gauss's law, an equation with no time derivative, and the spatial components are the evolution equations; the identity is what ties the time derivative of the constraint to the divergence of the evolution equations, so that the constraint, once imposed, is preserved. Counting the degrees of freedom, four equations less one identity less one gauge freedom leaves two, the two polarizations of the free field, which is the count the corpus's *Canonical Quantization of the Biquaternion Maxwell Field* reproduces from the constraint algebra.

**The source is forced to be conserved.** Sourcing the equation, $E^\nu = j^\nu$, and taking the divergence, gives

$$
\partial_\nu j^\nu = \partial_\nu E^\nu \equiv 0 .
$$

The conservation of the source is therefore not an independent law but an **integrability condition**: the equation has no solution unless the source is conserved. This is the second-theorem route to charge conservation. The corpus reaches the same conclusion inside the biquaternion algebra, where the single equation $\tilde{\nabla}\tilde{F}=-\tilde{R}$ requires $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{R})=0$, which expands to $\partial_t\rho+\mathrm{div}\,\mathbf{J}=0$; the identity of the second theorem and the biquaternion integrability condition are the same statement in two notations.

## Worked Example: a Local Symmetry with a Rigid Subgroup

The Maxwell local symmetry has no algebraic part, so it carries no charge at all. The opposite case is a local symmetry that does contain a rigid subgroup, and it shows how the identity and the first theorem coexist.

**The variational problem.** Let the fields be $A_\mu$ and a scalar $B$, and let the density be

$$
L = -\tfrac14 F_{\mu\nu}F^{\mu\nu} + \frac{m^2}{2}\bigl(A_\mu + \partial_\mu B\bigr)\bigl(A^\mu + \partial^\mu B\bigr),
$$

the Stueckelberg form of the massive vector field, in which the mass term is written so that a local symmetry survives.

**The local symmetry.** Under

$$
\delta A_\mu = \partial_\mu\varepsilon , \qquad \delta B = -\varepsilon ,
$$

the combination $A_\mu+\partial_\mu B$ is unchanged, and so is $F_{\mu\nu}$; the density is therefore exactly invariant for every function $\varepsilon$, with $b_{A_\mu}=0$ and $b_B=-1$. Here $b_B\neq0$, so restricting to constant $\varepsilon$ leaves the rigid transformation $\delta B=-\varepsilon$, a genuine shift symmetry of the scalar.

**The identity.** With $E^{A_\nu}=\partial_\mu F^{\mu\nu} - m^2(A^\nu+\partial^\nu B)$ and $E_B = -m^2\partial_\mu(A^\mu+\partial^\mu B)$, the first-order identity $b^iE_i - \partial_\mu(a^{i\mu}E_i)\equiv0$ reads

$$
-\,E_B - \partial_\nu E^{A_\nu} \equiv 0 ,
$$

and substitution gives $m^2\partial_\nu(A^\nu+\partial^\nu B) - m^2\partial_\nu(A^\nu+\partial^\nu B) - \partial_\nu\partial_\mu F^{\mu\nu}$, which vanishes by the same antisymmetry as before. The identity was checked on random smooth off-shell fields, with residual $9\times10^{-14}$ against a scale of $3.7$.

**The rigid current and the correction term.** The rigid subgroup, the shift of $B$, has the first-theorem current $j^\mu_{(B)} = L^\mu_B\,b_B = -m^2(A^\mu+\partial^\mu B)$, conserved on shell. Off shell the two theorems combine into the exact statement

$$
j^\mu_{(B)} + a^{A_\nu,\mu}E_{A_\nu} = -m^2\bigl(A^\mu+\partial^\mu B\bigr) + \bigl(\partial_\lambda F^{\lambda\mu} - m^2(A^\mu+\partial^\mu B)\bigr) = \partial_\lambda F^{\lambda\mu},
$$

whose divergence vanishes identically by the antisymmetry of $F$. So the second-theorem identity is exactly the statement that the rigid current, corrected by the term proportional to the other equation, is divergence-free **off shell**; on shell the correction term vanishes and the first theorem's conservation law stands alone.

**The role of the mass.** In the limit $m\to0$ the density reduces to the Maxwell density of the previous section, written in a redundant way, and the identity reduces to the Maxwell identity. The example therefore displays the two theorems as one mechanism at two values of a parameter, which is the reason it is worth keeping beside the Maxwell case.

## Counting: Conservation Laws against Identities

The two theorems are best kept apart by what they count.

**Definition.** A symmetry group is of **finite type** when its transformation is determined by finitely many constant parameters, and of **infinite type** when it depends on arbitrary functions. A symmetry of the first theorem is of finite type; a symmetry of the second theorem is of infinite type.

| Item | First theorem | Second theorem |
|---|---|---|
| Parameter | constant, $k$ of them | arbitrary function, $q$ of them |
| Assumption | $\delta L=\partial_\mu F^\mu$, $F$ built from the fields | $\delta L=\partial_\mu F^\mu$ for **all** $\varepsilon^\alpha$ |
| Conclusion | $k$ currents, $\partial_\mu j^\mu_a=0$ on shell | $q$ identities, $\equiv0$ off shell |
| On shell | new conserved charges | empty |
| Effect on the equations | none | $N-q$ independent equations, gauge freedom |
| Maxwell case | none (no rigid subgroup) | one identity, source conservation |
| Stueckelberg case | one rigid shift, one current | one identity, one constraint |

The distinction is not a matter of taste, and the count of the degrees of freedom makes it explicit. A first-kind symmetry adds no condition to the equations and yields one integral of the motion per parameter. A second-kind symmetry adds one differential identity per arbitrary function, removes that many independent equations, and opens the same number of gauge directions; it yields no integral of the motion unless it happens to contain a rigid subgroup, in which case the rigid part is governed by the first theorem and the local part by the second, as in the Stueckelberg example.

## The Hamiltonian Form

The corpus also states Noether's theorem on the Hamiltonian side, and the relation between the two statements is worth recording, because the Hamiltonian form is the first theorem in disguise. On a symplectic manifold with Hamiltonian $H$, a Lie group acting on the manifold and preserving both the symplectic form and $H$ has a momentum map $J$ whose components are conserved, $\{J_\xi,H\}=0$. The action is the first-kind action, the parameters are constants, and the conclusion is a family of conserved functions. The local, field-theoretic version of the same statement is the covariant Hamiltonian theory of *Multisymplectic and Covariant Hamiltonian Field Theory*, where the conserved scalar is replaced by a form; the second theorem's identity, by contrast, has no Hamiltonian counterpart of this shape, because it is not a statement about a conserved quantity at all.

## The Naming

**Definition (Weyl).** A symmetry is of the **first kind** when its parameters are constants, and of the **second kind** when its parameters are functions of the coordinates. Equivalently, a first-kind symmetry is a rigid subgroup of the symmetry group of the action, and a second-kind symmetry is the local, or gauge, part.

The names are frequently reversed in the literature and in informal use. The reversal is worth naming because it changes the theorem that is being invoked. A transformation written with an arbitrary function of position is **of the second kind**, and invoking "Noether's theorem" on it yields the second theorem, an identity, not a conservation law. A transformation written with a constant parameter is of the first kind, and only then does "Noether's theorem" yield a conserved current. The corpus's own gauge articles are of the second kind throughout: the localisation of the central $U(1)$ in *The Gauge Principle in Biquaternionic Form* produces the connection and the covariant derivative — the degeneracy described by the second theorem — and not a new conserved charge.

## Summary

Noether's two theorems classify the symmetries of an action by the nature of their parameters and return two different objects. A symmetry whose parameters are constants — of the first kind, $k$ of them — gives $k$ conserved currents $j^\mu_a = L^\mu_i\xi^i_a - F^\mu_a$, divergence-free on shell, and hence $k$ conserved charges. A symmetry whose parameters are arbitrary functions — of the second kind, $q$ of them — gives no charge: it gives $q$ differential identities among the Euler–Lagrange expressions, valid off shell, which say that the equations are not independent, that at most $N-q$ of them are independent, and that a gauge condition is needed to determine the evolution.

Both theorems follow from one identity, $\delta L = E_i\delta u^i + \partial_\mu(L^\mu_i\delta u^i)$, read with the two kinds of variation. The identity of the second theorem, $b^iE_i - \partial_\mu(a^{i\mu}E_i)\equiv0$ in the first-order case, is checked on the Maxwell field, where it is $\partial_\nu\partial_\mu F^{\mu\nu}\equiv0$ with residual exactly zero, and on a Stueckelberg-type field with a rigid subgroup, where it is verified to $9\times10^{-14}$ against a scale of $3.7$. The Maxwell identity forces the source to be conserved, $\partial_\nu j^\nu=0$, turning charge conservation into an integrability condition; the same conclusion is reached inside the biquaternion algebra from $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{R})=0$. A local symmetry contributes a conservation law only through a rigid subgroup, and it has one only when the algebraic part $b^i$ of its transformation does not vanish.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $u^i$, $i=1,\dots,N$ | Fields of the theory |
| $L(x,u,\partial u)$ | Lagrangian density |
| $S=\int L\,d^mx$ | Action |
| $\partial_\mu$ | Partial derivative with respect to $x^\mu$ |
| $L^\mu_i = \partial L/\partial u^i_{,\mu}$ | Derivative of the density with respect to the gradient of the field |
| $E_i = \partial L/\partial u^i - \partial_\mu L^\mu_i$ | Euler–Lagrange expression |
| $\Theta^\mu = L^\mu_i\,\delta u^i$ | Boundary current of a variation |
| $F^\mu$ | Divergence through which a symmetry changes the density, $\delta L=\partial_\mu F^\mu$ |
| $\xi^i$, $\xi^i_a$ | Generator of a first-kind symmetry |
| $a^{i\mu}$, $b^i$ | Coefficients of $\varepsilon$ and $\partial_\mu\varepsilon$ in a second-kind symmetry |
| $a^{i\mu_1\cdots\mu_k}$ | Coefficient of the $k$-th derivative of $\varepsilon$, $k\le r$ |
| $q$ | Number of arbitrary functions of a second-kind symmetry |
| $j^\mu$, $j^\mu_a$ | Noether currents |
| $Q=\int j^0\,d^{m-1}x$ | Noether charge |
| $T^\mu{}_\nu = L^\mu_i\partial_\nu u^i - \delta^\mu_\nu L$ | Canonical energy–momentum tensor |
| First kind | Rigid symmetry, constant parameters |
| Second kind | Local symmetry, arbitrary functions |
| On shell / off shell | $E_i=0$ / not imposing $E_i=0$ |
| $\Box = \partial_\mu\partial^\mu$ | d'Alembertian |

## Further Reading

- Emmy Noether, "Invariante Variationsprobleme", *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse* (1918), 235–257, the original paper, in which the two theorems are stated and proved as the first and second theorems of the theory of invariants of continuous groups.
- Hermann Weyl, "Gravitation und Elektrizität", *Sitzungsberichte der Preußischen Akademie der Wissenschaften* (1918), 465–480, for the distinction between symmetries of the first kind and of the second kind.
- Yvette Kosmann-Schwarzbach, *The Noether Theorems: Invariance and Conservation Laws in the Twentieth Century* (Springer, 2011), for the history, the two theorems and their reception.
- Peter J. Olver, *Applications of Lie Groups to Differential Equations* (Springer, 2nd ed. 1993), for the generalised Bianchi identities and the modern statement of the second theorem.
- Andrzej Trautman, "Noether equations and conservation laws", *Communications in Mathematical Physics* **6** (1967) 248–261, for the field-theoretic statement and the Einstein-tensor example.
- Katherine A. Brading and Harvey R. Brown, "Noether's theorems and gauge symmetries" (arXiv:hep-th/0009058, 2000), for the logical status of the second theorem in gauge theories and the distinction between a symmetry and a constraint.
- Herbert Goldstein, Charles P. Poole and John L. Safko, *Classical Mechanics* (Addison–Wesley, 3rd ed. 2002), for the first theorem in its mechanical setting.
- Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry* (Springer, 2nd ed. 1999), for the momentum map and the Hamiltonian form of the first theorem.
