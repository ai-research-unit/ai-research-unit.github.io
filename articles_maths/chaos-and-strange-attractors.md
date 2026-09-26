
# __Chaos and Strange Attractors__

## Introduction

**Chaos** is the property of a deterministic system whose orbits separate at an exponential rate and yet whose asymptotic behaviour is confined: it is the coexistence of sensitive dependence on the initial condition, which makes prediction at long range impossible, with recurrence, which makes the statistics of the motion stable and computable. **Strange attractors** are the invariant sets on which this behaviour occurs — compact, invariant, attracting a neighbourhood, not a finite union of submanifolds, with a fractal structure, and carrying an invariant measure whose entropy is positive and whose Lyapunov exponents are nonzero. The two notions are distinct: a hyperbolic set need not attract, and a chaotic invariant set need not be strange. The theory has a topological side — sensitivity, transitivity, the density of periodic orbits, Li–Yorke chaos and positive entropy — and a definition of the notion of attractor from *Topological Dynamics* and *Smooth Dynamical Systems*, and it has a measure-theoretic side — the Lyapunov exponents, the entropy, the SRB measures and the dimension — inherited from *Hyperbolic Dynamics and Anosov Systems* and *Ergodic Theory*.

The article begins with the definitions of chaos: sensitive dependence, the definition of Devaney by transitivity, dense periodic points and sensitivity, the theorem that the first two imply the third on a perfect compact metric space, and the notion of **Li–Yorke chaos** with its scrambled sets and its relation to positive entropy; the hierarchies are stated, with the theorem that positive entropy implies Li–Yorke chaos and the example of Smítal of a zero-entropy Li–Yorke chaotic interval map showing that the converse fails. The **attractors** are treated next: topological attractors and their basins, the Conley decomposition inherited from the chain recurrence, Milnor attractors, and the definition of a **strange attractor** as an attractor with sensitive dependence and a fractal structure. The examples follow: the solenoid of Smale, the Plykin and DA attractors of hyperbolic type, the **Lorenz attractor** of the system $\dot x=\sigma(y-x)$, $\dot y=x(\rho-z)-y$, $\dot z=xy-\beta z$, the geometric Lorenz model of Guckenheimer and Williams and the theorem of Tucker that the Lorenz attractor is a robust strange attractor, and the **Hénon attractor** of the map $(x,y)\mapsto(1-ax^2+y,bx)$. The **fractal dimension** is then developed: the Hausdorff and box dimensions, the middle-third Cantor set, the Kaplan–Yorke formula and the conjecture, proved in important cases by Ledrappier and Young, that the dimension of a hyperbolic attractor is the Kaplan–Yorke number; and the article closes with the statistics of a strange attractor — the SRB measure, the entropy and the physical measure — and with the relation of chaos to the entropy of *Topological Dynamics* and to the symbolic models.

The topological dynamics, the transitivity, the entropy, the recurrence and the mixing are those of *Topological Dynamics*; the flows, the linearisation, the structural stability and the attractors of the smooth theory are those of *Smooth Dynamical Systems*; the hyperbolicity, the Lyapunov exponents, the Pesin formula and the SRB measures are those of *Hyperbolic Dynamics and Anosov Systems*; the measure-preserving transformations, the ergodicity and the entropy are those of *Ergodic Theory*. The Hausdorff and box dimensions are standard real analysis and are defined in line with the citation of the standard literature, the fractal dimension being absent from the corpus. The symbolic models, the bifurcations that generate the attractors and the smooth systems with random perturbations belong to later categories of this Part.

No physics is invoked; the equations are given as differential equations and maps and no mechanical or physical interpretation is attached to them.

## Notions of Chaos

### Sensitive Dependence

**Definition.** Let $X$ be a compact metric space and $T:X\to X$ continuous. The system has **sensitive dependence on the initial condition** if there is $\delta>0$ such that for every $x \in X$ and every $\epsilon>0$ there is $y \in X$ with $d(x,y)<\epsilon$ and an $n \ge0$ with $d(T^nx,T^ny)>\delta$. The system is **chaotic in the sense of Devaney** if it is topologically transitive, its periodic points are dense, and it has sensitive dependence on the initial condition.

Sensitivity is the failure of the family of iterates to be equicontinuous: a rotation of the circle, or any equicontinuous system, is not sensitive, and the classification of the minimal equicontinuous systems as translations of *Topological Dynamics* is thus a classification of the minimal systems without chaos.

**Theorem (Banks–Brooks–Cairns–Davis–Stacey).** Let $X$ be a compact metric space with no isolated points and let $T:X\to X$ be continuous. If $T$ is topologically transitive and the periodic points of $T$ are dense in $X$, then $T$ has sensitive dependence on the initial condition. Consequently a transitive system with dense periodic points is chaotic in the sense of Devaney.

*Proof.* The theorem is the one proved in the paper cited below. The content of the hypothesis is exactly what the failure of sensitivity denies: if $T$ is not sensitive, then there are $\delta>0$, a point $x$ and a radius $\epsilon>0$ such that $d(T^nx,T^ny)\le\delta$ for every $y$ in the $\epsilon$-ball of $x$ and every $n \ge0$ — that is, the family of iterates is $\delta$-equicontinuous at $x$ — and the theorem states that this local equicontinuity is incompatible with the transitivity, the density of the periodic points and the absence of isolated points. The use of the last hypothesis is that it supplies a pair of distinct periodic points at positive distance whose images can be separated: without it the statement fails, since the transposition of a two-point space is transitive, has dense periodic points and is not sensitive, the ball of radius $\epsilon<d(a,b)$ around $a$ containing only $a$ itself. $\square$

### Li–Yorke Chaos and the Hierarchies

**Definition.** A pair $x,y$ is **$\delta$-scrambled** for $T$ if $\liminf_{n}d(T^nx,T^ny)=0$ and $\limsup_nd(T^nx,T^ny)>\delta$; the system is **chaotic in the sense of Li–Yorke** if there is an uncountable set $S$ such that every pair of distinct points of $S$ is $\delta$-scrambled for some $\delta>0$. The notion is the formalisation of the unpredictability of a pair of orbits that approach and separate infinitely often.

**Theorem (Li–Yorke).** Let $f:[0,1]\to[0,1]$ be continuous. If $f$ has a periodic orbit of period $3$, then $f$ is chaotic in the sense of Li–Yorke and, moreover, has periodic orbits of every period.

*Proof (sketch).* By the theorem of Sharkovskii the existence of a period-three orbit implies the existence of orbits of all periods; the uncountable scrambled set is constructed from the itinerary of the points with respect to the intervals determined by the period-three orbit, and the stretching of the intervals under the iterate of $f$ produces the two limit behaviours. $\square$

**Theorem (Blanchard–Glasner–Kolyada).** Let $T$ be a continuous map of a compact metric space with positive topological entropy. Then $T$ is chaotic in the sense of Li–Yorke; consequently positive entropy is a sufficient condition for chaos in the sense of Li–Yorke.

**Theorem (Smítal).** There is a continuous map of the interval with zero topological entropy which is chaotic in the sense of Li–Yorke; consequently the converse of the previous theorem fails, and the Li–Yorke notion and positive entropy are not equivalent even in dimension one.

**Remark (the hierarchy).** Two implications hold in general: positive topological entropy implies Li–Yorke chaos (Blanchard–Glasner–Kolyada), and transitivity together with the density of the periodic points implies sensitivity on a perfect space (Banks and others). The notions are not equivalent, however: the example of Smítal separates Li–Yorke chaos from positive entropy, since it has zero entropy, and the precise relations among the several definitions of chaos on a given class of systems are the subject of the literature cited below.

### The Horseshoe as the Model

**Example (the Smale horseshoe).** The horseshoe of *Smooth Dynamical Systems* has a hyperbolic invariant Cantor set on which the dynamics is conjugate to the full two-sided two-shift; it therefore has sensitive dependence (the shift separates points at the first coordinate where their sequences differ), dense periodic points, positive entropy $\log2$, and an uncountable scrambled set. Every one of the notions of chaos above is realised by the horseshoe, and the horseshoe is the model to which the chaotic invariant sets of *Hyperbolic Dynamics and Anosov Systems* reduce through the Markov partitions; the symbolic models are developed.

**Example (the doubling map and the shift).** The map $x\mapsto2x\bmod1$ of the circle has sensitive dependence with $\delta=\frac14$, dense periodic points and entropy $\log2$, and it is conjugate to the full two-shift on the complement of the countable set of dyadic rationals; it is a chaotic system in every sense above, and its periodic points are the rationals with odd denominators.

## Attractors and Strange Attractors

### Attractors and Their Basins

**Definition.** Let $M$ be a compact metric space and $T:M\to M$ continuous. A compact invariant set $A \subseteq M$ is an **attractor** if there is a neighbourhood $U$ of $A$ with $T(\bar U)\subseteq U$ and $A=\bigcap_{n\ge0}T^n(U)$ — a **trapping region** — and $T|_A$ is topologically transitive; the **basin** of $A$ is $\{x \in M:\omega(x)\subseteq A\}$, an open invariant set. A **Milnor attractor** is a compact invariant set $A$ such that the set of points whose $\omega$-limit set meets $A$ has positive measure with respect to a reference measure — for a diffeomorphism, the Riemannian volume — and $A$ is minimal with this property; the Milnor notion is weaker than the topological one and is the natural one for the attractors with a fractal structure, whose basin of attraction in the topological sense may be small.

**Proposition (attractors and chain recurrence).** Every attractor contains a chain transitive component and its basin is open and invariant; by Conley's theorem, every point of $M\setminus\mathrm{CR}(T)$ lies in the basin of some attractor, and the attractors are the maximal chain transitive pieces that can be isolated by a trapping region. This is Conley's decomposition of *Topological Dynamics*, and it gives the general framework in which the strange attractors sit.

### Strange Attractors

**Definition.** An attractor $A$ is **strange** if it is not a finite union of submanifolds of $M$, its restriction $T|_A$ has sensitive dependence on the initial condition, and it carries an invariant measure with a positive Lyapunov exponent; the last condition makes the strange attractor a **chaotic attractor** in the measure-theoretic sense as well. The definition is descriptive: the class is not closed under topological conjugacy in a way that is invariant under all the definitions in the literature, and the examples below are those for which the strong properties — hyperbolicity or its singular analogue, a positive exponent and a fractal dimension — have been established.

**Example (hyperbolic attractors).** (i) The **solenoid** of Smale is the attractor of a diffeomorphism of the solid torus that is the inverse limit of the doubling map of the circle: the attracting set is a hyperbolic attractor, homeomorphic to the inverse limit of the circle under $z\mapsto z^2$, locally the product of a Cantor set and an interval, and not a manifold; the restriction of the map to it is hyperbolic with a one-dimensional expanding direction and a Cantor set of contracting directions, and its entropy is $\log2$.

(ii) The **Plykin attractor** is a hyperbolic attractor of a diffeomorphism of the two-sphere with a finite number of holes, a one-dimensional expanding attractor whose stable manifolds foliate the basin; the **DA attractor** of Smale is obtained from an Anosov diffeomorphism by a surgery that turns a periodic orbit into a source and produces an attractor with a one-dimensional unstable direction.

(iii) The attractors of the hyperbolic type carry Bowen–Ruelle measures by the theory of *Hyperbolic Dynamics and Anosov Systems*, and their dimension is given by the Kaplan–Yorke formula in the cases covered by the theorem of Ledrappier and Young stated below.

**Example (the Lorenz attractor).** Consider the system

$$
\dot x=\sigma(y-x), \qquad \dot y=x(\rho-z)-y, \qquad \dot z=xy-\beta z ,
$$

with $\sigma=10$, $\rho=28$, $\beta=\frac83$. The origin is a hyperbolic equilibrium of saddle type whose eigenvalues are all real, namely $\lambda^2+11\lambda-270=0$ together with $-\beta$, that is $11.83$, $-22.83$ and $-2.67$; the two remaining equilibria have a pair of complex eigenvalues with positive real part, and numerically the orbits spiral in the two wings of a butterfly-shaped set and never settle: the set

$$
A=\bigcap_{t\ge0}\overline{\varphi([t,\infty)\times U)}
$$

for a suitable trapping region $U$ is the **Lorenz attractor**. The geometric model of Guckenheimer and Williams replaces the flow near the origin by a fixed linear behaviour and the return map by a one-dimensional map with a single discontinuity and a negative Schwarzian derivative, and in the model the attractor has sensitive dependence, a dense orbit, a countable set of periodic orbits, and a positive Lyapunov exponent; the attractor is not uniformly hyperbolic, because the equilibrium inside it has a direction of contraction, and the appropriate notion is that of a **singular hyperbolic** attractor, in which the expansion of the volume along the invariant directions dominates the contraction and is uniform away from the equilibrium. The theorem of Tucker establishes by rigorous computation that the Lorenz attractor is a genuine strange attractor of the system: the trapping region is absorbing for the given parameters, the return map is well defined and uniformly expanding on its domain, and the attractor has a positive Lyapunov exponent and a fractal structure, so the system is chaotic and the attractor is robust under perturbations of the parameters.

**Example (the Hénon attractor).** The **Hénon map** is the diffeomorphism of the plane

$$
(x,y)\mapsto(1-ax^2+y,\ bx),
$$

which for $a=1.4$, $b=0.3$ has a compact invariant set that attracts an open set and is numerically a fractal curve of dimension slightly above $1$; the map is not uniformly hyperbolic, and the existence of the strange attractor for a positive measure set of parameters $(a,b)$ with $b$ small is the theorem of Benedicks and Carleson and of Benedicks and Young, in which the attractor is shown to have a positive Lyapunov exponent, an SRB measure and a dimension strictly between $1$ and $2$; the SRB measure of the Hénon attractor and its dimension were obtained by Benedicks and Young. The map is a diffeomorphism with $\det Df=-b$ constant, and hence the two Lyapunov exponents of any invariant measure satisfy $\lambda_1+\lambda_2=\log|b|$ exactly; at $a=1.4$, $b=0.3$ the numerical exponents are $\lambda_1\approx0.4192$ and $\lambda_2\approx-1.6232$, whose sum is $-1.2040$, in agreement with the exact value $\log0.3=-1.2040$ to four decimal places.

## Fractal Dimension

### Hausdorff and Box Dimension

**Definition.** Let $A$ be a subset of a metric space. For $s \ge0$ and $\delta>0$ put

$$
H^s_\delta(A)=\inf\Bigl\{\sum_{i}(\operatorname{diam}U_i)^s : A \subseteq\bigcup_iU_i,\ \operatorname{diam}U_i<\delta\Bigr\},
\qquad H^s(A)=\lim_{\delta\to0}H^s_\delta(A),
$$

the **Hausdorff measure** of dimension $s$; there is a unique $s_0$ with $H^s(A)=\infty$ for $s<s_0$ and $H^s(A)=0$ for $s>s_0$, namely the **Hausdorff dimension** $\dim_HA$. The **box dimension** is

$$
\dim_BA=\lim_{\delta\to0}\frac{\log N_\delta(A)}{-\log\delta},
$$

when the limit exists, with $N_\delta(A)$ the least number of sets of diameter $\le\delta$ needed to cover $A$; its upper and lower variants always exist, and the inequality

$$
\dim_HA\le\underline{\dim}_BA\le\overline{\dim}_BA
$$

holds. The Hausdorff dimension is countably stable, $\dim_H\bigcup_kA_k=\sup_k\dim_HA_k$, while the box dimension is only finitely stable; neither is a topological invariant, and the theory is that of the standard literature on fractal geometry, cited below.

**Example.** The middle-third Cantor set $C \subseteq[0,1]$ satisfies $C=\frac13C\cup(\frac23+\frac13C)$, the two pieces being disjoint, so $H^s(C)=2\cdot3^{-s}H^s(C)$ for the critical value and $H^s(C)$ is finite and nonzero only for $s=\log2/\log3$; hence

$$
\dim_HC=\dim_BC=\frac{\log2}{\log3}=0.630929\ldots
$$

and the measure $H^s$ with $s=\log2/\log3$ is positive and finite on $C$. The same computation gives the dimension of the self-similar sets of an iterated function system as the solution of $\sum_i\rho_i^s=1$ when the open set condition holds, which is the content of the Moran–Hutchinson theorem.

### The Kaplan–Yorke Formula and the Dimension of an Attractor

**Definition.** Let $\mu$ be an ergodic invariant measure of a $C^1$ diffeomorphism with Lyapunov exponents $\lambda_1\ge\cdots\ge\lambda_d$ and $j$ the largest index with $\lambda_1+\cdots+\lambda_j \ge0$ (so that $j<d$ unless the measure is volume-preserving with all the sums nonnegative). The **Kaplan–Yorke number** is

$$
D_{KY}=j+\frac{\lambda_1+\cdots+\lambda_j}{|\lambda_{j+1}|} .
$$

**Theorem (Ledrappier–Young).** Let $f$ be a $C^{1+\alpha}$ diffeomorphism of a surface and let $\mu$ be an ergodic hyperbolic measure with a positive exponent and an SRB property. Then the Hausdorff dimension of $\mu$ — the infimum of the Hausdorff dimensions of the sets of full measure — satisfies the **dimension formula** of Ledrappier and Young, and in the case in which the unstable distribution is one-dimensional and the measure is the SRB measure, it equals the Kaplan–Yorke number $1+\lambda_1/|\lambda_2|$; the equality of the Hausdorff dimension of a hyperbolic attractor with the Kaplan–Yorke number is the **Kaplan–Yorke conjecture**, proved in this and in more general settings by the dimension theory of the invariant measures.

**Example (the Hénon attractor continued).** With $\lambda_1\approx0.4192$, $\lambda_2\approx-1.6232$ the Kaplan–Yorke number is

$$
D_{KY}=1+\frac{0.4192}{1.6232}=1.2583 ,
$$

and the numerically computed box dimension of the Hénon attractor at $a=1.4$, $b=0.3$ is approximately $1.26$, in agreement with the formula; the attractor therefore has a non-integer dimension strictly between $1$ and $2$, which is the quantitative form of its strangeness.

## The Statistics of a Strange Attractor

**Theorem (SRB measures and physical measures).** Let $A$ be a hyperbolic attractor or a singular hyperbolic attractor of the Lorenz type, and let $T$ be the map or the time-one map of the flow. Then the Bowen–Ruelle measure $\mu$ of *Hyperbolic Dynamics and Anosov Systems* is an invariant probability measure on $A$, it is ergodic, and it is mixing when $T|_A$ is topologically mixing; its entropy satisfies Pesin's formula $h_\mu=\sum\lambda_i^+$, and its basin has positive measure with respect to the Riemannian volume; such a measure is a **physical measure**, in that for a positive-measure set of initial conditions the Birkhoff averages converge to the averages with respect to $\mu$, so that the statistics of the orbit are computable even though the individual orbit is unpredictable. The entropy, the mixing and the decay of correlations of $\mu$ are those of *Ergodic Theory*, and the symbolic model of the attractor by a subshift of finite type, obtained from a Markov partition, is .

**Corollary (chaos and entropy).** For a chaotic attractor whose SRB measure has a positive Lyapunov exponent, the entropy of that measure is positive, by Pesin's formula, and hence the system is chaotic in the sense of Li–Yorke by the theorem of Blanchard–Glasner–Kolyada of the first section; the dimension, the entropy and the exponents of a strange attractor are thus three quantitative invariants linked by Pesin's formula and by the Kaplan–Yorke formula, and the computation of any two of them determines the third, up to the identification of the measure.

**Remark (the role of the attractor).** A hyperbolic set which is not attracting is invisible to the statistics of a typical orbit, but it is the invariant set that persists under perturbations and that is detected by the periodic orbits; a strange attractor is exactly a hyperbolic, or singular hyperbolic, invariant set that attracts, so that it has both the structural robustness of the hyperbolic theory and the statistical relevance of an attractor. The interplay of these two properties — robustness under perturbation and absolute continuity of the invariant measure on the unstable manifolds — is the content of the theory of the physical measures and is the reason why the Lorenz and Hénon attractors, though not uniformly hyperbolic, are the prototypes of the observed chaos.

## Summary

Chaos is the conjunction of sensitive dependence on the initial condition — there is $\delta>0$ such that every point has arbitrarily close companions whose orbits separate by $\delta$ at some time — with recurrence. **Devaney chaos** requires topological transitivity, dense periodic points and sensitivity; on a perfect compact metric space transitivity and dense periodic points already imply sensitivity, by the theorem of Banks–Brooks–Cairns–Davis–Stacey. **Li–Yorke chaos** requires an uncountable set whose pairs are $\delta$-scrambled ($\liminf$ of the distance $0$ and $\limsup$ above $\delta$); positive topological entropy implies Li–Yorke chaos, by Blanchard–Glasner–Kolyada, while Smítal's zero-entropy interval map is Li–Yorke chaotic, so the converse fails; the horseshoe, the doubling map and the shifts realise all the notions, and the symbolic models belong. The **attractors** are the compact transitive invariant sets with a trapping region and an open bas; the **Milnor attractor** relaxes the topological basin to a positive-measure condition; and a **strange attractor** is an attractor that is not a finite union of submanifolds, has sensitive dependence and carries an invariant measure with a positive exponent. The hyperbolic attractors — the solenoid, the Plykin and the DA attractors — the **Lorenz attractor**, whose geometric model of Guckenheimer and Williams is a singular hyperbolic attractor and which the theorem of Tucker proves to be a robust strange attractor of the system $\dot x=\sigma(y-x)$, $\dot y=x(\rho-z)-y$, $\dot z=xy-\beta z$ at $\sigma=10$, $\rho=28$, $\beta=\frac83$, and the **Hénon attractor** of the map $(x,y)\mapsto(1-ax^2+y,bx)$ at $a=1.4$, $b=0.3$ are the examples.

The **Hausdorff dimension** $\dim_HA$ is the critical exponent of the Hausdorff measure, the **box dimension** counts the covering sets, and $\dim_H\le\underline{\dim}_B\le\overline{\dim}_B$; the middle-third Cantor set has dimension $\log2/\log3=0.630929\ldots$. The **Kaplan–Yorke number** $D_{KY}=j+(\lambda_1+\cdots+\lambda_j)/|\lambda_{j+1}|$ is conjectured to be the Hausdorff dimension of a hyperbolic attractor and is proved to be so, for surface diffeomorphisms and SRB measures, by the dimension theory of Ledrappier and Young; for the Hénon attractor the exponents satisfy $\lambda_1+\lambda_2=\log|b|$ exactly and $D_{KY}=1.2583$, in agreement with the numerical box dimension $\approx1.26$. The statistics of a strange attractor are carried by its **SRB (physical) measure**, ergodic and mixing in the standard examples, with Pesin's formula $h_\mu=\sum\lambda_i^+$; the positivity of the exponent gives positive entropy and hence Li–Yorke chaos, and the entropy, the exponents and the dimension are the three quantitative invariants of the attractor, linked by Pesin's formula and the Kaplan–Yorke formula.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\delta$ | sensitivity constant; scrambling constant |
| $S$ | scrambled set of Li–Yorke chaos |
| $A$, $U$ | attractor and trapping region |
| $\omega(x)$ | limit set, defining the basin |
| $\dim_H$, $\dim_B$ | Hausdorff and box dimension |
| $H^s$, $H^s_\delta$ | Hausdorff measure and its outer approximation |
| $N_\delta(A)$ | least number of $\delta$-sets covering $A$ |
| $\lambda_1\ge\cdots\ge\lambda_d$ | Lyapunov exponents |
| $D_{KY}$ | Kaplan–Yorke number |
| $\mu$ | SRB (physical) measure |
| $h_\mu$ | measure-theoretic entropy |
| $\sigma,\rho,\beta$ | parameters of the Lorenz system |
| $a,b$ | parameters of the Hénon map |
| $C$ | middle-third Cantor set |



## Further Reading

- John Banks, Jeffrey Brooks, Grant Cairns, Gary Davis and Peter Stacey, "On Devaney's definition of chaos", *American Mathematical Monthly* 99 (1992), 332–334, for the theorem that transitivity and dense periodic points imply sensitivity.
- Tien-Yien Li and James A. Yorke, "Period three implies chaos", *American Mathematical Monthly* 82 (1975), 985–992, for Li–Yorke chaos and the scrambled sets.
- François Blanchard, Eli Glasner and Sergiy Kolyada, "On Li–Yorke pairs", *Journal für die reine und angewandte Mathematik* 547 (2002), 51–68, for the theorem that positive entropy implies Li–Yorke chaos.
- Jaroslav Smítal, "Chaotic functions with zero topological entropy", *Transactions of the American Mathematical Society* 297 (1986), 269–282, for the zero-entropy Li–Yorke chaotic interval maps.
- John Guckenheimer and Philip Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields* (Springer, 1983), for the geometric Lorenz model and the analysis of the Lorenz equations.
- Warwick Tucker, "A rigorous ODE solver and Smale's 14th problem", *Foundations of Computational Mathematics* 2 (2002), 53–117, for the proof that the Lorenz attractor is a genuine strange attractor.
- Michael Benedicks and Lennart Carleson, "The dynamics of the Hénon map", *Annals of Mathematics* 133 (1991), 73–169, for the existence of the strange attractor of the Hénon family.
- Michael Benedicks and Lai-Sang Young, "Sinai–Bowen measures for certain Hénon maps", *Inventiones Mathematicae* 112 (1993), 541–576, for the SRB measure and the dimension of the Hénon attractor.
- François Ledrappier and Lai-Sang Young, "The metric entropy of diffeomorphisms I, II", *Annals of Mathematics* 122 (1985), 509–574, and "Dimension formula for random transformations", *Communications in Mathematical Physics* 117 (1988), 529–548, for the dimension formula and the Kaplan–Yorke conjecture.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications* (Wiley, 1990), for the Hausdorff and box dimensions and the self-similar sets.
- James C. Robinson, *Dimensions, Embeddings, and Attractors* (Cambridge University Press, 2011), for the theory of the dimension of attractors and the Lyapunov exponents.
